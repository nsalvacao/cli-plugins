"""Tests for generator.plugin_generator -- plugin generator."""

import json
import re
from pathlib import Path

import pytest

from generator.plugin_generator import (
    build_trigger_phrases,
    compute_stats,
    format_flags_table,
    generate_commands_md,
    generate_examples_md,
    generate_plugin,
    generate_plugin_json,
    generate_scan_cli_md,
    generate_skill_md,
    group_commands,
    load_cli_map,
    walk_tree,
)

FIXTURE_DIR = Path(__file__).resolve().parents[1] / "output"
CF_JSON = FIXTURE_DIR / "claude-flow.json"
DOCKER_JSON = FIXTURE_DIR / "docker.json"


@pytest.fixture
def cf_map():
    """Load claude-flow.json as a dict."""
    if not CF_JSON.exists():
        pytest.skip(f"{CF_JSON} not available (output/ is gitignored)")
    return load_cli_map(CF_JSON)


@pytest.fixture
def cf_stats(cf_map):
    return compute_stats(cf_map)


# ---------------------------------------------------------------------------
# load_cli_map
# ---------------------------------------------------------------------------


class TestLoadCliMap:
    def test_valid(self, cf_map):
        assert cf_map["cli_name"] == "claude-flow"
        assert "commands" in cf_map
        assert "metadata" in cf_map

    def test_missing_fields(self, tmp_path):
        bad = tmp_path / "bad.json"
        bad.write_text(json.dumps({"cli_name": "x"}))
        with pytest.raises(ValueError, match="Missing required keys"):
            load_cli_map(bad)

    def test_invalid_json(self, tmp_path):
        bad = tmp_path / "bad.json"
        bad.write_text("not json")
        with pytest.raises(json.JSONDecodeError):
            load_cli_map(bad)


# ---------------------------------------------------------------------------
# compute_stats
# ---------------------------------------------------------------------------


class TestComputeStats:
    def test_counts(self, cf_stats):
        assert cf_stats.total_commands >= 30  # at least top-level + subs
        assert cf_stats.total_flags >= 5
        assert cf_stats.total_examples >= 10  # unique examples
        assert cf_stats.global_flags == 8
        assert cf_stats.cli_name == "claude-flow"
        assert cf_stats.version.startswith("3.1.0-alpha.")

    def test_max_depth(self, cf_stats):
        assert cf_stats.max_depth >= 1

    def test_top_commands(self, cf_stats):
        assert "agent" in cf_stats.top_commands
        assert "swarm" in cf_stats.top_commands
        assert "memory" in cf_stats.top_commands


# ---------------------------------------------------------------------------
# walk_tree / group_commands
# ---------------------------------------------------------------------------


class TestTreeHelpers:
    def test_walk_tree_yields_all(self, cf_map):
        names = [name for name, _, _ in walk_tree(cf_map["commands"])]
        assert "doctor" in names
        assert "route" in names

    def test_walk_tree_depths(self, cf_map):
        depths = {name: d for name, _, d in walk_tree(cf_map["commands"])}
        assert depths["agent"] == 0  # top-level
        # subcommands of route should be depth 1
        assert depths.get("stats", -1) == 1

    def test_group_commands(self, cf_map):
        grps = group_commands(cf_map["commands"])
        assert "Command Groups" in grps or "Commands" in grps
        all_cmds = []
        for v in grps.values():
            all_cmds.extend(v)
        assert "doctor" in all_cmds


# ---------------------------------------------------------------------------
# format_flags_table
# ---------------------------------------------------------------------------


class TestFormatFlagsTable:
    def test_empty(self):
        assert format_flags_table([]) == ""

    def test_renders_rows(self):
        flags = [
            {"name": "--verbose", "short": "-v", "type": "bool", "description": "Enable verbose"},
        ]
        table = format_flags_table(flags)
        assert "| Flag |" in table
        assert "`--verbose`" in table
        assert "`-v`" in table

    def test_default_value(self):
        flags = [
            {
                "name": "--fix",
                "short": "-f",
                "type": "bool",
                "description": "Fix issues",
                "default": "false",
            },
        ]
        table = format_flags_table(flags)
        assert "default: false" in table


# ---------------------------------------------------------------------------
# generate_plugin_json
# ---------------------------------------------------------------------------


class TestPluginJson:
    def test_valid_json(self, cf_map, cf_stats):
        content = generate_plugin_json(cf_map, cf_stats)
        obj = json.loads(content)
        assert obj["name"] == "cli-claude-flow"
        assert obj["version"] == cf_map["cli_version"]
        assert "keywords" in obj
        assert "claude-flow" in obj["keywords"]

    def test_description(self, cf_map, cf_stats):
        content = generate_plugin_json(cf_map, cf_stats)
        obj = json.loads(content)
        assert "claude-flow" in obj["description"]


# ---------------------------------------------------------------------------
# generate_skill_md
# ---------------------------------------------------------------------------


class TestSkillMd:
    def test_frontmatter(self, cf_map, cf_stats):
        md = generate_skill_md(cf_map, cf_stats)
        assert md.startswith("---\n")
        # Must have name field
        assert "\nname: " in md.split("---")[1], "SKILL.md must have name in frontmatter"
        # Extract frontmatter description
        match = re.search(r"description:\s*>-\n\s+(.+?)(?:\n---)", md, re.DOTALL)
        assert match, "SKILL.md must have frontmatter description"
        desc = match.group(1).strip()
        assert len(desc) <= 1024, f"Description too long: {len(desc)} chars"

    def test_word_count(self, cf_map, cf_stats):
        md = generate_skill_md(cf_map, cf_stats)
        # Strip frontmatter
        body = re.sub(r"^---.*?---\n", "", md, flags=re.DOTALL)
        words = len(body.split())
        assert 200 <= words <= 3000, f"Word count {words} out of range"

    def test_no_second_person(self, cf_map, cf_stats):
        md = generate_skill_md(cf_map, cf_stats)
        # Check body (after frontmatter) for second person
        body = re.sub(r"^---.*?---\n", "", md, flags=re.DOTALL)
        violations = re.findall(
            r"\b(you should|you can|you need|you must|you will)\b",
            body,
            re.IGNORECASE,
        )
        assert not violations, f"Second person found: {violations}"

    def test_contains_stats(self, cf_map, cf_stats):
        md = generate_skill_md(cf_map, cf_stats)
        assert str(cf_stats.total_commands) in md
        assert str(cf_stats.global_flags) in md

    def test_contains_commands(self, cf_map, cf_stats):
        md = generate_skill_md(cf_map, cf_stats)
        assert "claude-flow agent" in md
        assert "claude-flow swarm" in md


# ---------------------------------------------------------------------------
# generate_commands_md
# ---------------------------------------------------------------------------


class TestCommandsMd:
    def test_all_top_commands(self, cf_map):
        md = generate_commands_md(cf_map)
        for name in cf_map["commands"]:
            assert name in md, f"Command '{name}' missing from commands.md"

    def test_flags_table(self, cf_map):
        md = generate_commands_md(cf_map)
        # doctor has flags
        assert "| Flag |" in md

    def test_global_flags(self, cf_map):
        md = generate_commands_md(cf_map)
        assert "Global Flags" in md

    def test_subcommands_listed(self, cf_map):
        md = generate_commands_md(cf_map)
        # route has subcommands like stats, feedback
        assert "route stats" in md or "route coverage" in md


# ---------------------------------------------------------------------------
# generate_examples_md
# ---------------------------------------------------------------------------


class TestExamplesMd:
    def test_has_examples(self, cf_map):
        md = generate_examples_md(cf_map)
        assert "```bash" in md

    def test_deduplicates(self, cf_map):
        md = generate_examples_md(cf_map)
        # Count occurrences of a common example
        count = md.count("claude-flow doctor\n")
        assert count <= 1, "Examples should be deduplicated"

    def test_escapes_backticks_in_example_descriptions(self):
        cli_map = {
            "cli_name": "demo",
            "commands": {
                "run": {
                    "path": "demo run",
                    "examples": ["demo run --fast", "Handle fenced text ```inline``` safely"],
                    "subcommands": {},
                }
            },
            "metadata": {},
        }
        md = generate_examples_md(cli_map)
        assert md.count("```") == 2
        assert "```inline```" not in md

    def test_fallback_examples_from_usage_when_none_explicit(self):
        cli_map = {
            "cli_name": "pnpm",
            "commands": {
                "add": {
                    "path": "pnpm add",
                    "usage_pattern": "Usage: pnpm add <name>",
                    "description": "Install package dependencies",
                    "examples": [],
                    "subcommands": {},
                },
                "install": {
                    "path": "pnpm install",
                    "usage_pattern": "Usage: pnpm install [options]",
                    "description": "Install project dependencies",
                    "examples": [],
                    "subcommands": {},
                },
            },
            "metadata": {},
        }
        md = generate_examples_md(cli_map)
        assert "pnpm add <name>" in md
        assert "pnpm install [options]" in md
        assert "_No explicit examples found in CLI help" in md


# ---------------------------------------------------------------------------
# generate_scan_cli_md
# ---------------------------------------------------------------------------


class TestScanCliMd:
    def test_contains_cli_name(self):
        md = generate_scan_cli_md("claude-flow", "output/claude-flow.json")
        assert "claude-flow" in md
        assert "$CLAUDE_PLUGIN_ROOT" in md

    def test_frontmatter(self):
        md = generate_scan_cli_md("docker", "output/docker.json")
        assert "---\nname: scan-cli" in md


# ---------------------------------------------------------------------------
# build_trigger_phrases
# ---------------------------------------------------------------------------


class TestTriggerPhrases:
    def test_length(self, cf_map):
        desc = build_trigger_phrases("claude-flow", cf_map)
        assert len(desc) <= 1024

    def test_content(self, cf_map):
        desc = build_trigger_phrases("claude-flow", cf_map)
        assert "claude-flow" in desc
        # Should include some command names
        assert any(cmd in desc for cmd in ["agent", "swarm", "memory", "init"])


# ---------------------------------------------------------------------------
# Full pipeline (integration)
# ---------------------------------------------------------------------------


class TestFullPipeline:
    def test_generate_plugin_creates_files(self, cf_map, tmp_path):
        root = generate_plugin(cf_map, tmp_path, "output/claude-flow.json")
        assert root.exists()
        assert (root / ".claude-plugin" / "plugin.json").exists()
        assert (root / "skills" / "cli-claude-flow" / "SKILL.md").exists()
        assert (root / "skills" / "cli-claude-flow" / "references" / "commands.md").exists()
        assert (root / "skills" / "cli-claude-flow" / "references" / "examples.md").exists()
        assert (root / "commands" / "scan-cli.md").exists()
        assert (root / "scripts" / "rescan.sh").exists()

    def test_rescan_script_uses_entrypoints_with_module_fallback(self, cf_map, tmp_path):
        root = generate_plugin(cf_map, tmp_path, "output/claude-flow.json")
        script = (root / "scripts" / "rescan.sh").read_text(encoding="utf-8")

        assert 'cli-crawler "$CLI_NAME" -o "$JSON_PATH"' in script
        assert 'python3 -m crawler.pipeline "$CLI_NAME" -o "$JSON_PATH"' in script
        assert 'generate-plugin "$JSON_PATH" -o "$PROJECT_ROOT/plugins" "$@"' in script
        assert (
            'python3 -m generator.plugin_generator "$JSON_PATH" -o "$PROJECT_ROOT/plugins" "$@"'
            in script
        )
        assert "scripts/generate_plugin.py" not in script

    def test_idempotent(self, cf_map, tmp_path):
        generate_plugin(cf_map, tmp_path, "output/claude-flow.json")
        # Read first run
        skill1 = (
            tmp_path / "cli-claude-flow" / "skills" / "cli-claude-flow" / "SKILL.md"
        ).read_text()
        # Run again
        generate_plugin(cf_map, tmp_path, "output/claude-flow.json")
        skill2 = (
            tmp_path / "cli-claude-flow" / "skills" / "cli-claude-flow" / "SKILL.md"
        ).read_text()
        assert skill1 == skill2

    def test_dry_run_no_files(self, cf_map, tmp_path):
        root = generate_plugin(cf_map, tmp_path, "output/claude-flow.json", dry_run=True)
        assert not root.exists()

    def test_plugin_json_valid(self, cf_map, tmp_path):
        root = generate_plugin(cf_map, tmp_path, "output/claude-flow.json")
        pj = json.loads((root / ".claude-plugin" / "plugin.json").read_text())
        assert pj["name"] == "cli-claude-flow"

    @pytest.mark.skipif(not DOCKER_JSON.exists(), reason="docker.json not available")
    def test_generality_docker(self, tmp_path):
        docker_map = load_cli_map(DOCKER_JSON)
        root = generate_plugin(docker_map, tmp_path, "output/docker.json")
        assert (root / ".claude-plugin" / "plugin.json").exists()
        assert (root / "skills" / "cli-docker" / "SKILL.md").exists()
        pj = json.loads((root / ".claude-plugin" / "plugin.json").read_text())
        assert pj["name"] == "cli-docker"
