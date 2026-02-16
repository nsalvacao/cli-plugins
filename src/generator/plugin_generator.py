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
import os
import re
import textwrap
from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

from lib.cli_identity import plugin_slug

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
    cli_slug: str = ""


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

REQUIRED_KEYS = {"cli_name", "commands", "metadata"}


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
    tree = cli_map["commands"]

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
        version=cli_map.get("cli_version", "unknown"),
        cli_name=cli_map["cli_name"],
        cli_slug=plugin_slug(cli_map["cli_name"]),
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
    tree = cli_map["commands"]

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


KEYWORD_STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "these",
    "those",
    "into",
    "over",
    "under",
    "through",
    "using",
    "used",
    "use",
    "tool",
    "tools",
    "command",
    "commands",
    "subcommand",
    "subcommands",
    "option",
    "options",
    "flag",
    "flags",
    "manage",
    "manages",
    "management",
    "execute",
    "executing",
    "run",
    "runs",
    "running",
    "show",
    "shows",
    "list",
    "lists",
    "help",
    "cli",
}

COMPACT_SKILL_TOKEN_BUDGET = 800
COMPACT_SKILL_MAX_EXAMPLES = 5


def generate_semantic_keywords(cli_map: dict, max_keywords: int = 8) -> list[str]:
    """Generate semantic keywords from CLI name, command groups, and domain terms."""
    cli_name = str(cli_map.get("cli_name", "")).strip().lower()
    if not cli_name:
        return []

    keywords: list[str] = [cli_name]
    seen: set[str] = {cli_name}
    cli_parts = {part for part in re.split(r"[-_]", cli_name) if part}

    commands = cli_map.get("commands", {})

    # Prioritize command groups (nodes with subcommands) by breadth.
    command_groups: list[tuple[int, str]] = []
    for name, data in commands.items():
        subcommands = data.get("subcommands", {})
        if subcommands:
            command_groups.append((len(subcommands), name.lower()))
    for _size, group_name in sorted(command_groups, key=lambda item: (-item[0], item[1])):
        normalized = group_name.strip()
        if (
            not normalized
            or normalized in seen
            or normalized in KEYWORD_STOPWORDS
            or normalized in cli_parts
        ):
            continue
        keywords.append(normalized)
        seen.add(normalized)
        if len(keywords) >= max_keywords:
            return keywords[:max_keywords]

    # Then mine domain terms from full descriptions (not only first words).
    frequencies: Counter[str] = Counter()
    for _name, data, depth in walk_tree(commands):
        description = _clean_description(data.get("description", "")).lower()
        if not description:
            continue
        weight = 2 if depth == 0 else 1
        for token in re.findall(r"[a-z][a-z0-9-]{2,}", description):
            normalized = token.strip("-")
            if (
                not normalized
                or normalized in seen
                or normalized in KEYWORD_STOPWORDS
                or normalized in cli_parts
            ):
                continue
            frequencies[normalized] += weight

    for token, _count in frequencies.most_common():
        keywords.append(token)
        seen.add(token)
        if len(keywords) >= max_keywords:
            break

    return keywords[:max_keywords]


def _resolve_author(author: str | None) -> str | None:
    """Resolve author from explicit arg or environment variable."""
    if author is not None and author.strip():
        return author.strip()
    env_author = os.getenv("CLI_PLUGINS_AUTHOR", "").strip()
    return env_author or None


def _build_author_metadata(author: str) -> dict[str, str]:
    """Create plugin author metadata from a string."""
    match = re.match(r"^\s*([^<]+?)\s*<([^>]+)>\s*$", author)
    if match:
        name, email = match.groups()
        return {"name": name.strip(), "email": email.strip()}
    return {"name": author}


def _approx_token_count(text: str) -> int:
    """Approximate token count for compactness checks."""
    return len(re.findall(r"\w+|[^\w\s]", text))


def _escape_triple_backticks(text: str) -> str:
    """Prevent accidental markdown fence breaks in generated docs."""
    return text.replace("```", r"\`\`\`")


def _example_command_from_usage(path: str, usage: str, cli_name: str) -> str:
    """Build a safe command example from usage/path without hallucinating."""
    normalized_usage = re.sub(r"\s+", " ", usage.strip())
    if normalized_usage:
        normalized_usage = re.sub(r"(?i)^usage:\s*", "", normalized_usage).strip()
        if normalized_usage.startswith(cli_name) and len(normalized_usage) <= 160:
            return normalized_usage
    return path.strip()


def _collect_document_examples(
    cli_map: dict,
    *,
    limit: int | None = None,
) -> tuple[list[tuple[str, int, str, str]], bool]:
    """Collect examples for docs.

    Returns:
        (entries, has_explicit_examples)
        entries = list of (path, depth, command_example, description)
    """
    cli = cli_map["cli_name"]
    entries: list[tuple[str, int, str, str]] = []
    seen: set[str] = set()

    # Prefer explicit examples extracted from help.
    for name, data, depth in walk_tree(cli_map["commands"]):
        path = data.get("path", f"{cli} {name}")
        raw = data.get("examples", [])
        for i in range(0, len(raw) - 1, 2):
            cmd, desc = raw[i], raw[i + 1]
            key = cmd.strip()
            if not key or key in seen:
                continue
            seen.add(key)
            entries.append((path, depth, key, _clean_description(desc)))
            if limit is not None and len(entries) >= limit:
                return entries, True

    if entries:
        return entries, True

    # Fallback: synthesize examples from usage/path when explicit examples don't exist.
    fallback_note = "Generated from command usage (CLI help has no explicit EXAMPLES section)."
    for name, data, depth in walk_tree(cli_map["commands"]):
        path = data.get("path", f"{cli} {name}")
        usage = data.get("usage_pattern", "")
        cmd = _example_command_from_usage(path, usage, cli)
        key = cmd.strip()
        if not key or key in seen:
            continue
        seen.add(key)
        desc = _clean_description(data.get("description", "")) or fallback_note
        entries.append((path, depth, key, desc))
        if limit is not None and len(entries) >= limit:
            break

    return entries, False


# ---------------------------------------------------------------------------
# Template generators
# ---------------------------------------------------------------------------


def generate_plugin_json(cli_map: dict, stats: Stats, author: str | None = None) -> str:
    """Generate .claude-plugin/plugin.json content."""
    cli = stats.cli_name
    cli_slug = stats.cli_slug
    keywords = generate_semantic_keywords(cli_map)

    obj = {
        "name": f"cli-{cli_slug}",
        "version": stats.version,
        "description": f"Command reference plugin for {cli} CLI",
        "keywords": keywords,
        "repository": "https://github.com/nsalvacao/cli-plugins",
        "license": "MIT",
    }
    resolved_author = _resolve_author(author)
    if resolved_author:
        obj["author"] = _build_author_metadata(resolved_author)
    return json.dumps(obj, indent=2) + "\n"


def generate_skill_md(cli_map: dict, stats: Stats) -> str:
    """Generate the main SKILL.md file in compact progressive-disclosure form."""
    cli = stats.cli_name
    cli_slug = stats.cli_slug
    trigger = (
        f"This skill should be used when the user needs help with {cli} CLI commands, "
        "flags, and troubleshooting."
    )

    # Compact top-level command summary (no long descriptions).
    command_groups = sorted(
        name for name, data in cli_map["commands"].items() if data.get("subcommands")
    )
    leaf_commands = sorted(
        name for name, data in cli_map["commands"].items() if not data.get("subcommands")
    )

    command_examples: list[str] = []
    for preferred in ("agent", "swarm"):
        if preferred in cli_map["commands"]:
            command_examples.append(preferred)
    for candidate in sorted(cli_map["commands"].keys()):
        if candidate not in command_examples:
            command_examples.append(candidate)
        if len(command_examples) >= 3:
            break

    # Global flags table
    gf_table = format_flags_table(cli_map.get("global_flags", []))
    if not gf_table:
        gf_table = "_No global flags detected._"

    # Compact usage examples (first 5 unique examples).
    examples_lines: list[str] = []
    doc_examples, _has_explicit_examples = _collect_document_examples(
        cli_map, limit=COMPACT_SKILL_MAX_EXAMPLES
    )
    for _path, _depth, cmd, desc in doc_examples:
        safe_cmd = _escape_triple_backticks(cmd)
        safe_desc = _escape_triple_backticks(desc)
        examples_lines.append(f"```bash\n{safe_cmd}\n```\n{safe_desc}\n")
    examples_block = "\n".join(examples_lines) if examples_lines else "_No examples extracted._"

    def _render_top_level_section(group_limit: int, leaf_limit: int) -> str:
        lines: list[str] = []
        if command_groups:
            shown_groups = command_groups[:group_limit]
            lines.append("Command Groups:")
            lines.append(", ".join(f"`{name}`" for name in shown_groups))
            if len(shown_groups) < len(command_groups):
                lines.append(
                    f"... +{len(command_groups) - len(shown_groups)} more in `references/commands.md`"
                )
        if leaf_commands:
            shown_leaf = leaf_commands[:leaf_limit]
            lines.append("Standalone Commands:")
            lines.append(", ".join(f"`{name}`" for name in shown_leaf))
            if len(shown_leaf) < len(leaf_commands):
                lines.append(
                    f"... +{len(leaf_commands) - len(shown_leaf)} more in `references/commands.md`"
                )
        lines.append(
            "Command format examples: " + ", ".join(f"`{cli} {name}`" for name in command_examples)
        )
        return "\n".join(lines) if lines else "_No commands._"

    def _render_skill_md(group_limit: int, leaf_limit: int) -> str:
        top_commands_section = _render_top_level_section(group_limit, leaf_limit)
        parts: list[str] = []
        parts.append(f"---\nname: cli-{cli_slug}\ndescription: >-\n  {trigger}\n---\n")
        parts.append(f"# {cli} CLI Reference\n")
        parts.append(f"Compact command reference for **{cli}** v{stats.version}.\n")
        parts.append(
            f"- **{stats.total_commands}** total commands\n"
            f"- **{stats.total_flags}** command flags + **{stats.global_flags}** global flags\n"
            f"- **{stats.total_examples}** extracted usage examples\n"
            f"- Max nesting depth: {stats.max_depth}\n"
        )
        parts.append("## When to Use\n")
        parts.append(
            f"- Constructing or validating `{cli}` commands\n"
            f"- Looking up flags/options fast\n"
            f"- Troubleshooting failed invocations\n"
        )
        parts.append("## Top-Level Commands\n")
        parts.append(top_commands_section + "\n")
        parts.append("### Global Flags\n")
        parts.append(gf_table + "\n")
        parts.append("## Common Usage Patterns (Compact)\n")
        parts.append(examples_block)
        parts.append(
            "## Detailed References\n\n"
            "- Full command tree: `references/commands.md`\n"
            "- Full examples catalog: `references/examples.md`\n"
        )
        parts.append("## Re-Scanning\n")
        parts.append("After a CLI update, run `/scan-cli` or execute crawler + generator again.\n")
        return "\n".join(parts)

    group_limit = max(1, len(command_groups))
    leaf_limit = max(1, len(leaf_commands))
    skill_md = _render_skill_md(group_limit, leaf_limit)

    # Keep shrinking command lists until compact budget is met.
    while _approx_token_count(skill_md) > COMPACT_SKILL_TOKEN_BUDGET:
        changed = False
        if leaf_limit > 8:
            leaf_limit = max(8, leaf_limit - 8)
            changed = True
        elif group_limit > 4:
            group_limit = max(4, group_limit - 2)
            changed = True
        if not changed:
            break
        skill_md = _render_skill_md(group_limit, leaf_limit)

    return skill_md


def generate_commands_md(cli_map: dict) -> str:
    """Generate references/commands.md -- full command tree as markdown."""
    cli = cli_map["cli_name"]
    lines: list[str] = [f"# {cli} -- Complete Command Reference\n"]

    # Global flags
    gf = cli_map.get("global_flags", [])
    if gf:
        lines.append("## Global Flags\n")
        lines.append(format_flags_table(gf))
        lines.append("")

    # Group by top-level
    grps = group_commands(cli_map["commands"])
    for label, cmd_names in grps.items():
        lines.append(f"## {label}\n")
        for name in cmd_names:
            data = cli_map["commands"][name]
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
    cli = cli_map["cli_name"]
    lines: list[str] = [f"# {cli} -- Usage Examples\n"]
    doc_examples, has_explicit_examples = _collect_document_examples(cli_map)
    if not has_explicit_examples and doc_examples:
        lines.append("_No explicit examples found in CLI help; generated from usage patterns._\n")

    grouped: dict[tuple[str, int], list[tuple[str, str]]] = {}
    group_order: list[tuple[str, int]] = []
    for path, depth, cmd, desc in doc_examples:
        key = (path, depth)
        if key not in grouped:
            grouped[key] = []
            group_order.append(key)
        grouped[key].append((cmd, desc))

    for path, depth in group_order:
        header_level = "##" if depth == 0 else "###"
        lines.append(f"{header_level} `{path}`\n")
        for cmd, desc in grouped[(path, depth)]:
            safe_cmd = _escape_triple_backticks(cmd)
            safe_desc = _escape_triple_backticks(desc)
            lines.append(f"```bash\n{safe_cmd}\n```\n{safe_desc}\n")

    return "\n".join(lines) + "\n"


def generate_rescan_sh(
    cli_name: str,
    crawler_path: str,
    *,
    plugin_slug_name: str | None = None,
) -> str:
    """Generate scripts/rescan.sh -- executable rescan wrapper."""
    resolved_slug = plugin_slug_name or plugin_slug(cli_name)
    return textwrap.dedent(f"""\
    #!/usr/bin/env bash
    # Re-scan {cli_name} CLI and regenerate this plugin.
    # Usage: bash scripts/rescan.sh [--dry-run]
    set -euo pipefail

    SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"
    PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

    CLI_NAME="{cli_name}"
    JSON_PATH="$PROJECT_ROOT/output/$CLI_NAME.json"
    PLUGIN_DIR="$PROJECT_ROOT/plugins/cli-{resolved_slug}"

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
    author: str | None = None,
    dry_run: bool = False,
) -> Path:
    """Create the full plugin directory structure."""
    stats = compute_stats(cli_map)
    cli = stats.cli_name
    cli_slug = stats.cli_slug
    plugin_root = Path(output_dir) / f"cli-{cli_slug}"

    # Define all output paths
    files: dict[Path, str] = {}

    files[plugin_root / ".claude-plugin" / "plugin.json"] = generate_plugin_json(
        cli_map, stats, author=author
    )
    files[plugin_root / "skills" / f"cli-{cli_slug}" / "SKILL.md"] = generate_skill_md(
        cli_map, stats
    )
    files[plugin_root / "skills" / f"cli-{cli_slug}" / "references" / "commands.md"] = (
        generate_commands_md(cli_map)
    )
    files[plugin_root / "skills" / f"cli-{cli_slug}" / "references" / "examples.md"] = (
        generate_examples_md(cli_map)
    )
    files[plugin_root / "commands" / "scan-cli.md"] = generate_scan_cli_md(cli, crawler_path)
    files[plugin_root / "scripts" / "rescan.sh"] = generate_rescan_sh(
        cli,
        crawler_path,
        plugin_slug_name=cli_slug,
    )

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
    parser.add_argument(
        "--author",
        help=(
            "Plugin author name (or 'Name <email>'). "
            "If omitted, falls back to CLI_PLUGINS_AUTHOR env var. "
            "If neither is set, author field is omitted."
        ),
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
        author=args.author,
        dry_run=args.dry_run,
    )
    print(f"{'[DRY RUN] Would create' if args.dry_run else 'Generated'} plugin at: {plugin_root}")


if __name__ == "__main__":
    main()
