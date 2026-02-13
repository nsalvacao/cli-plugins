from crawler.models import CLIMap, Command, Flag


def test_flag_schema():
    """T006/T044: Flag should match data-model.md fields."""
    f = Flag(
        name="--help",
        long_name="--help",
        short_name="-h",
        type="bool",
        description="Show help",
        required=True,
        default="False",
        choices=None,
        confidence=1.0,
    )
    assert f.name == "--help"
    assert f.long_name == "--help"
    assert f.short_name == "-h"
    assert f.type == "bool"
    # Ensure backward compat or explicit break? Explicit break preferred for V1.
    # assert not hasattr(f, "short")  # Old field should be gone


def test_command_schema():
    """T006: Command should match data-model.md fields."""
    cmd = Command(
        path="docker run",
        name="run",
        description="Run a container",
        usage_pattern="docker run [OPTIONS] IMAGE",
        aliases=["r"],
        flags=[],
        positional_args=[],
        env_vars=[],
        subcommands={},
    )
    assert cmd.name == "run"
    assert cmd.path == "docker run"
    assert cmd.aliases == ["r"]
    # Check hierarchy
    assert isinstance(
        cmd.subcommands, dict
    )  # Implementation detail: dict is fine for internal model


def test_climap_schema():
    """T006: CLIMap should match data-model.md fields."""
    climap = CLIMap(
        cli_name="docker",
        cli_version="24.0.0",
        metadata={"author": "unknown", "scanned_at": "2023-01-01"},
        global_flags=[],
        environment_variables=[],
        commands={},
    )
    assert climap.cli_name == "docker"
    assert climap.cli_version == "24.0.0"
    assert climap.metadata["author"] == "unknown"
    # Old fields check
    assert not hasattr(climap, "cli")
    assert not hasattr(climap, "version")
    assert not hasattr(climap, "meta")
