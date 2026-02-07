"""Data structures for CLI crawler. Single source of truth for all shapes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Flag:
    name: str
    short: Optional[str] = None
    type: str = "string"  # "bool" | "string" (v1)
    required: bool = False
    default: Optional[str] = None
    choices: Optional[list[str]] = None
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
    description: str = ""
    usage_pattern: str = ""
    aliases: list[str] = field(default_factory=list)
    group: Optional[str] = None
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
class Meta:
    total_commands: int = 0
    total_flags: int = 0
    max_depth: int = 0
    parse_errors: int = 0
    parse_warnings: list[str] = field(default_factory=list)
    duration_seconds: float = 0.0


@dataclass
class CLIMap:
    cli: str
    version: str = ""
    scanned_at: str = ""
    help_pattern: str = ""
    global_flags: list[Flag] = field(default_factory=list)
    env_vars: list[EnvVar] = field(default_factory=list)
    tree: dict[str, Command] = field(default_factory=dict)
    meta: Meta = field(default_factory=Meta)


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
