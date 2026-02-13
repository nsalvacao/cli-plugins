#!/usr/bin/env python3
"""Generate a Claude Code plugin from a CLI crawler JSON map.

Usage:
    python scripts/generate_plugin.py output/claude-flow.json
    python scripts/generate_plugin.py output/docker.json -o ./my-plugins/
    python scripts/generate_plugin.py output/claude-flow.json --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import textwrap
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class Stats:
    total_commands: int = 0
    total_flags: int = 0
    total_examples: int = 0
    global_flags: int = 0
    commands_with_subcommands: int = 0
    max_depth: int = 0
    groups: list[str] = field(default_factory=list)
    top_commands: list[str] = field(default_factory=list)
    version: str = ""
    cli_name: str = ""


# ---------------------------------------------------------------------------
# Tree helpers
# ---------------------------------------------------------------------------


def walk_tree(tree: dict, depth: int = 0) -> Iterator[tuple[str, dict, int]]:
    """Yield (name, data, depth) for every node in the command tree."""
    for name, data in sorted(tree.items()):
        yield name, data, depth
        subs = data.get("subcommands", {})
        if subs:
            yield from walk_tree(subs, depth + 1)


def group_commands(tree: dict) -> dict[str, list[str]]:
    """Group top-level commands into 'Command Groups' (have subcommands)
    and 'Commands' (leaf nodes)."""
    groups: dict[str, list[str]] = {}
    for name, data in sorted(tree.items()):
        has_subs = bool(data.get("subcommands"))
        label = "Command Groups" if has_subs else "Commands"
        groups.setdefault(label, []).append(name)
    return groups


# ---------------------------------------------------------------------------
# Loading & stats
# ---------------------------------------------------------------------------

REQUIRED_KEYS = {"cli", "tree", "meta"}


def load_cli_map(path: str | Path) -> dict:
    """Read JSON, validate required top-level keys."""
    path = Path(path)
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    missing = REQUIRED_KEYS - set(data.keys())
    if missing:
        raise ValueError(f"Missing required keys in CLI map: {missing}")
    return data


def compute_stats(cli_map: dict) -> Stats:
    """Walk the tree to compute aggregate statistics."""
    tree = cli_map["tree"]

    total_commands = 0
    total_flags = 0
    commands_with_subs = 0
    max_depth = 0
    seen_examples: set[str] = set()

    for _name, data, depth in walk_tree(tree):
        total_commands += 1
        total_flags += len(data.get("flags", []))
        raw = data.get("examples", [])
        for i in range(0, len(raw) - 1, 2):
            seen_examples.add(raw[i].strip())
        if data.get("subcommands"):
            commands_with_subs += 1
        if depth > max_depth:
            max_depth = depth

    total_examples = len(seen_examples)

    global_flags = len(cli_map.get("global_flags", []))
    grps = group_commands(tree)
    top_cmds = sorted(tree.keys())

    return Stats(
        total_commands=total_commands,
        total_flags=total_flags,
        total_examples=total_examples,
        global_flags=global_flags,
        commands_with_subcommands=commands_with_subs,
        max_depth=max_depth,
        groups=list(grps.keys()),
        top_commands=top_cmds,
        version=cli_map.get("version", "unknown"),
        cli_name=cli_map["cli"],
    )


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------


def format_flags_table(flags: list[dict]) -> str:
    """Render a list of flags as a markdown table."""
    if not flags:
        return ""
    rows = ["| Flag | Short | Type | Description |", "| --- | --- | --- | --- |"]
    for f in flags:
        name = f.get("name", "")
        short = f.get("short", "")
        ftype = f.get("type", "")
        desc = f.get("description", "")
        default = f.get("default")
        if default is not None:
            desc += f" (default: {default})"
        rows.append(f"| `{name}` | `{short}` | {ftype} | {desc} |")
    return "\n".join(rows)


def build_trigger_phrases(cli_name: str, cli_map: dict) -> str:
    """Auto-generate a description string from the CLI name and top commands.
    Must be under 1024 characters for SKILL.md frontmatter."""
    tree = cli_map["tree"]

    # Build domain-aware grouping from commands with subcommands
    groups: list[str] = []
    leaves: list[str] = []
    for name, data in sorted(tree.items()):
        if data.get("subcommands"):
            desc = data.get("description", "").strip()
            # Summarize the group: "agent management", "swarm coordination", etc.
            if desc:
                short = desc.split(".")[0].split(",")[0].lower().strip()
                if len(short) < 50:
                    groups.append(f"{name} ({short})")
                else:
                    groups.append(name)
            else:
                groups.append(name)
        else:
            leaves.append(name)

    # Build natural-language description
    base = (
        f"This skill should be used when the user needs help with {cli_name} CLI "
        f"commands, including "
    )
    suffix = (
        f". Covers flags, subcommands, usage patterns, and troubleshooting "
        f"for all {len(tree)} {cli_name} commands."
    )

    budget = 1024 - len(base) - len(suffix)
    # Prioritize groups (more informative), then leaf commands
    parts: list[str] = []
    for item in groups + leaves:
        candidate = ", ".join(parts + [item])
        if len(candidate) > budget:
            break
        parts.append(item)

    return base + ", ".join(parts) + suffix


def _clean_description(desc: str) -> str:
    """Strip decorative prefixes/suffixes and runtime artifacts from crawler descriptions."""
    # Remove emoji prefixes, box-drawing chars, bracketed info/warn tags
    desc = re.sub(r"^[\u2500-\u257f═━\s]+", "", desc)
    desc = re.sub(r"[\u2500-\u257f═━\s]+$", "", desc)
    desc = re.sub(r"^\[(INFO|WARN|ERROR)\]\s*", "", desc)
    desc = re.sub(r"^[📋🔐⚡️🧠🪲🚀📚🔗♾️📈🧹📘🛡️❓]+\s*", "", desc)
    desc = re.sub(r"^\.\.+\s*", "", desc)
    # Strip stderr deprecation warnings captured as descriptions
    if re.match(r"^Flag shorthand .* has been deprecated", desc):
        return ""
    # Strip runtime status messages (e.g. "[STOPPED]", "Checking V3 progress...")
    if re.match(r"^(Claude Flow|Checking)\b.*\.\.\.", desc):
        return ""
    if re.search(r"\[(STOPPED|RUNNING|OK)\]", desc):
        return ""
    return desc.strip() or desc


# ---------------------------------------------------------------------------
# Template generators
# ---------------------------------------------------------------------------


def generate_plugin_json(cli_map: dict, stats: Stats) -> str:
    """Generate .claude-plugin/plugin.json content."""
    cli = stats.cli_name
    # Extract keywords from top commands (first 5) + cli name
    keywords = [cli]
    # Add unique meaningful words from descriptions
    seen: set[str] = {cli}
    for data in cli_map["tree"].values():
        for word in data.get("description", "").lower().split():
            word = re.sub(r"[^a-z0-9-]", "", word)
            if len(word) > 3 and word not in seen:
                keywords.append(word)
                seen.add(word)
            if len(keywords) >= 6:
                break
        if len(keywords) >= 6:
            break

    obj = {
        "name": f"cli-{cli}",
        "version": stats.version,
        "description": f"Command reference plugin for {cli} CLI",
        "keywords": keywords,
        "author": {
            "name": "Nuno Salvacao",
            "email": "nuno.salvacao@gmail.com",
            "url": "https://github.com/nsalvacao",
        },
        "repository": "https://github.com/nsalvacao/cli-plugins",
        "license": "MIT",
    }
    return json.dumps(obj, indent=2) + "\n"


def generate_skill_md(cli_map: dict, stats: Stats) -> str:
    """Generate the main SKILL.md file."""
    cli = stats.cli_name
    trigger = build_trigger_phrases(cli, cli_map)

    # Build quick reference table -- all top-level commands
    quick_ref_rows = ["| Command | Description |", "| --- | --- |"]
    for name in stats.top_commands:
        data = cli_map["tree"].get(name, {})
        desc = _clean_description(data.get("description", ""))
        quick_ref_rows.append(f"| `{cli} {name}` | {desc} |")
    quick_ref = "\n".join(quick_ref_rows)

    # Global flags table
    gf_table = format_flags_table(cli_map.get("global_flags", []))

    # Command groups summary
    grps = group_commands(cli_map["tree"])
    groups_section = ""
    for label, cmds in grps.items():
        groups_section += f"\n### {label}\n\n"
        groups_section += ", ".join(f"`{c}`" for c in cmds) + "\n"

    # Common usage examples (pick first 8 unique examples from tree)
    examples_lines: list[str] = []
    seen_ex: set[str] = set()
    for _, data, _ in walk_tree(cli_map["tree"]):
        raw = data.get("examples", [])
        for i in range(0, len(raw) - 1, 2):
            cmd, desc = raw[i], raw[i + 1]
            if cmd not in seen_ex:
                seen_ex.add(cmd)
                examples_lines.append(f"```bash\n{cmd}\n```\n{desc}\n")
            if len(examples_lines) >= 8:
                break
        if len(examples_lines) >= 8:
            break
    examples_block = "\n".join(examples_lines)

    parts: list[str] = []
    parts.append(f"---\nname: cli-{cli}\ndescription: >-\n  {trigger}\n---\n")
    parts.append(f"# {cli} CLI Reference\n")
    parts.append(f"Expert command reference for **{cli}** v{stats.version}.\n")
    parts.append(
        f"- **{stats.total_commands}** commands "
        f"({stats.commands_with_subcommands} with subcommands)\n"
        f"- **{stats.total_flags}** command flags + "
        f"**{stats.global_flags}** global flags\n"
        f"- **{stats.total_examples}** usage examples\n"
        f"- Max nesting depth: {stats.max_depth}\n"
    )
    parts.append("## When to Use\n")
    parts.append(
        f"This skill applies when:\n"
        f"- Constructing or validating `{cli}` commands\n"
        f"- Looking up flags, options, or subcommands\n"
        f"- Troubleshooting `{cli}` invocations or errors\n"
        f"- Needing correct syntax for `{cli}` operations\n"
    )
    parts.append("## Prerequisites\n")
    # Only suggest npm install for node-based CLIs; otherwise generic
    npm_clis = {"claude-flow", "langchain", "ag-kit"}
    if cli in npm_clis:
        parts.append(f"Install {cli}:\n```bash\nnpm install -g {cli}@latest\n```\n")
    else:
        parts.append(f"Ensure `{cli}` is installed and available on PATH.\n")
    parts.append("## Quick Reference\n")
    parts.append(quick_ref + "\n")
    parts.append("### Global Flags\n")
    parts.append(gf_table + "\n")
    parts.append("## Command Overview\n")
    parts.append(groups_section)
    parts.append("## Common Usage Patterns\n")
    parts.append(examples_block)
    parts.append(
        "## Detailed References\n\n"
        "For complete command documentation including all flags and subcommands:\n"
        "- **Full command tree:** see `references/commands.md`\n"
        "- **All usage examples:** see `references/examples.md`\n"
    )
    troubleshooting = "## Troubleshooting\n\n"
    has_doctor = "doctor" in cli_map["tree"]
    if has_doctor:
        troubleshooting += f"- Run `{cli} doctor` to diagnose issues\n"
    troubleshooting += (
        f"- Use `{cli} --help` or `{cli} <command> --help` for inline help\n"
        "- Add `--verbose` for detailed output during debugging\n"
    )
    parts.append(troubleshooting)
    parts.append(
        "## Re-scanning\n\n"
        "To update this plugin after a CLI version change, run the `/scan-cli` command\n"
        "or manually execute the crawler and generator.\n"
    )
    return "\n".join(parts)


def generate_commands_md(cli_map: dict) -> str:
    """Generate references/commands.md -- full command tree as markdown."""
    cli = cli_map["cli"]
    lines: list[str] = [f"# {cli} -- Complete Command Reference\n"]

    # Global flags
    gf = cli_map.get("global_flags", [])
    if gf:
        lines.append("## Global Flags\n")
        lines.append(format_flags_table(gf))
        lines.append("")

    # Group by top-level
    grps = group_commands(cli_map["tree"])
    for label, cmd_names in grps.items():
        lines.append(f"## {label}\n")
        for name in cmd_names:
            data = cli_map["tree"][name]
            desc = _clean_description(data.get("description", ""))
            path = data.get("path", f"{cli} {name}")
            lines.append(f"### `{path}`\n")
            lines.append(f"{desc}\n")

            # Usage pattern
            usage = data.get("usage_pattern")
            if usage:
                lines.append(f"```\n{usage}\n```\n")

            # Flags
            flags = data.get("flags", [])
            if flags:
                lines.append(format_flags_table(flags))
                lines.append("")

            # Subcommands
            subs = data.get("subcommands", {})
            if subs:
                lines.append("**Subcommands:**\n")
                for sub_name, sub_data in sorted(subs.items()):
                    sub_desc = _clean_description(sub_data.get("description", ""))
                    sub_path = sub_data.get("path", f"{path} {sub_name}")
                    lines.append(f"#### `{sub_path}`\n")
                    lines.append(f"{sub_desc}\n")

                    sub_flags = sub_data.get("flags", [])
                    if sub_flags:
                        lines.append(format_flags_table(sub_flags))
                        lines.append("")

                    # Sub-subcommands (depth 2)
                    sub_subs = sub_data.get("subcommands", {})
                    if sub_subs:
                        for ss_name, ss_data in sorted(sub_subs.items()):
                            ss_desc = _clean_description(ss_data.get("description", ""))
                            ss_path = ss_data.get("path", f"{sub_path} {ss_name}")
                            lines.append(f"##### `{ss_path}`\n")
                            lines.append(f"{ss_desc}\n")

    return "\n".join(lines) + "\n"


def generate_examples_md(cli_map: dict) -> str:
    """Generate references/examples.md -- all usage examples."""
    cli = cli_map["cli"]
    lines: list[str] = [f"# {cli} -- Usage Examples\n"]
    seen: set[str] = set()

    for name, data, depth in walk_tree(cli_map["tree"]):
        raw = data.get("examples", [])
        if not raw:
            continue

        path = data.get("path", f"{cli} {name}")
        header_level = "##" if depth == 0 else "###"
        section_lines: list[str] = []

        for i in range(0, len(raw) - 1, 2):
            cmd, desc = raw[i], raw[i + 1]
            key = cmd.strip()
            if key in seen:
                continue
            seen.add(key)
            section_lines.append(f"```bash\n{cmd}\n```\n{desc}\n")

        if section_lines:
            lines.append(f"{header_level} `{path}`\n")
            lines.extend(section_lines)

    return "\n".join(lines) + "\n"


def generate_rescan_sh(cli_name: str, crawler_path: str) -> str:
    """Generate scripts/rescan.sh -- executable rescan wrapper."""
    return textwrap.dedent(f"""\
    #!/usr/bin/env bash
    # Re-scan {cli_name} CLI and regenerate this plugin.
    # Usage: bash scripts/rescan.sh [--dry-run]
    set -euo pipefail

    SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"
    PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

    CLI_NAME="{cli_name}"
    JSON_PATH="$PROJECT_ROOT/output/$CLI_NAME.json"
    PLUGIN_DIR="$PROJECT_ROOT/plugins/cli-$CLI_NAME"

    # Check CLI is available
    if ! command -v "$CLI_NAME" &>/dev/null; then
        echo "ERROR: $CLI_NAME not found on PATH. Install it first." >&2
        exit 1
    fi

    echo "==> Crawling $CLI_NAME..."
    python3 "$PROJECT_ROOT/cli_crawler.py" "$CLI_NAME"

    echo "==> Generating plugin..."
    python3 "$PROJECT_ROOT/scripts/generate_plugin.py" "$JSON_PATH" "$@"

    echo "==> Done. Plugin at: $PLUGIN_DIR"
    ls -la "$PLUGIN_DIR"
    """)


def generate_scan_cli_md(cli_name: str, crawler_path: str = "") -> str:
    """Generate commands/scan-cli.md slash command."""
    return textwrap.dedent(f"""\
    ---
    name: scan-cli
    description: Re-scan the {cli_name} CLI and regenerate plugin reference files
    allowed-tools: ["Bash"]
    ---

    # Re-scan {cli_name} CLI

    Run the rescan script to crawl the CLI and regenerate this plugin:

    ```bash
    bash $CLAUDE_PLUGIN_ROOT/scripts/rescan.sh
    ```

    Add `--dry-run` to preview without writing files:

    ```bash
    bash $CLAUDE_PLUGIN_ROOT/scripts/rescan.sh --dry-run
    ```

    ## Notes

    - Requires `{cli_name}` installed and on PATH
    - Idempotent -- re-running overwrites existing files cleanly
    """)


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def generate_plugin(
    cli_map: dict,
    output_dir: str | Path,
    crawler_path: str,
    *,
    dry_run: bool = False,
) -> Path:
    """Create the full plugin directory structure."""
    stats = compute_stats(cli_map)
    cli = stats.cli_name
    plugin_root = Path(output_dir) / f"cli-{cli}"

    # Define all output paths
    files: dict[Path, str] = {}

    files[plugin_root / ".claude-plugin" / "plugin.json"] = generate_plugin_json(cli_map, stats)
    files[plugin_root / "skills" / f"cli-{cli}" / "SKILL.md"] = generate_skill_md(cli_map, stats)
    files[plugin_root / "skills" / f"cli-{cli}" / "references" / "commands.md"] = (
        generate_commands_md(cli_map)
    )
    files[plugin_root / "skills" / f"cli-{cli}" / "references" / "examples.md"] = (
        generate_examples_md(cli_map)
    )
    files[plugin_root / "commands" / "scan-cli.md"] = generate_scan_cli_md(cli, crawler_path)
    files[plugin_root / "scripts" / "rescan.sh"] = generate_rescan_sh(cli, crawler_path)

    if dry_run:
        log.info("Dry run -- would create:")
        for p in sorted(files.keys()):
            log.info("  %s (%d bytes)", p, len(files[p].encode()))
        return plugin_root

    # Write files
    for p, content in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        log.info("Wrote %s", p)

    # Make rescan.sh executable
    rescan_path = plugin_root / "scripts" / "rescan.sh"
    rescan_path.chmod(rescan_path.stat().st_mode | 0o755)

    log.info("Plugin generated at %s", plugin_root)
    return plugin_root


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    try:
        from importlib.metadata import version

        pkg_version = version("cli-plugins")
    except Exception:
        pkg_version = "0.0.0-dev"

    parser = argparse.ArgumentParser(
        prog="generate-plugin",
        description="Generate a Claude Code plugin from a CLI crawler JSON map.",
    )
    parser.add_argument("--version", action="version", version=f"generate-plugin {pkg_version}")
    parser.add_argument(
        "json_path",
        help="Path to the crawler JSON file (e.g. output/claude-flow.json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="plugins",
        help="Output directory for the plugin (default: plugins/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview output paths without writing files",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    cli_map = load_cli_map(args.json_path)
    plugin_root = generate_plugin(
        cli_map,
        args.output,
        args.json_path,
        dry_run=args.dry_run,
    )
    print(f"{'[DRY RUN] Would create' if args.dry_run else 'Generated'} plugin at: {plugin_root}")


if __name__ == "__main__":
    main()
