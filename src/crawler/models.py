"""Data structures for CLI crawler. Single source of truth for all shapes."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Flag:
    name: str
    long_name: str | None = None
    short_name: str | None = None
    type: str = "string"  # "bool" | "string" (v1)
    required: bool = False
    default: str | None = None
    choices: list[str] | None = None
    description: str = ""
    confidence: float = 0.5


@dataclass
class PositionalArg:
    name: str
    required: bool = False
    description: str = ""


@dataclass
class EnvVar:
    name: str
    description: str = ""


@dataclass
class Command:
    path: str  # "git commit"
    name: str  # "commit"
    description: str = ""
    usage_pattern: str = ""
    aliases: list[str] = field(default_factory=list)
    group: str | None = None
    deprecated: bool = False
    hidden: bool = False
    dynamic: bool = False
    positional_args: list[PositionalArg] = field(default_factory=list)
    flags: list[Flag] = field(default_factory=list)
    env_vars: list[EnvVar] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)
    global_flags_inherited: bool = True
    subcommands: dict[str, Command] = field(default_factory=dict)
    confidence: float = 0.5


@dataclass
class CLIMap:
    cli_name: str
    cli_version: str = ""
    metadata: dict[str, str] = field(default_factory=dict)
    global_flags: list[Flag] = field(default_factory=list)
    environment_variables: list[EnvVar] = field(default_factory=list)
    commands: dict[str, Command] = field(default_factory=dict)


@dataclass
class ExecutionResult:
    stdout: str
    stderr: str
    exit_code: int
    command: list[str]
    timed_out: bool = False
    duration: float = 0.0


@dataclass
class HelpDetectionResult:
    pattern: str  # "--help", "-h", "help", "bare"
    result: ExecutionResult
    is_manpage: bool = False


@dataclass
class ParseResult:
    command: Command
    subcommand_names: list[str] = field(default_factory=list)
    subcommand_descriptions: dict[str, str] = field(default_factory=dict)
    raw_help: str = ""
    warnings: list[str] = field(default_factory=list)
