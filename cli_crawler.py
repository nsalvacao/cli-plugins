#!/usr/bin/env python3
"""Universal CLI Help Crawler - OpenAPI for CLIs.

Crawls CLI --help outputs and generates structured JSON maps
that AI agents can use for precise command reasoning.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from crawler.config import CLIConfig, CrawlerConfig, load_config
from crawler.pipeline import crawl_all, crawl_cli


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crawl CLI --help outputs and generate structured JSON maps",
        epilog="Examples:\n"
        "  python cli_crawler.py git -o output/git.json\n"
        "  python cli_crawler.py --config config.yaml --all\n"
        "  python cli_crawler.py docker -v --include-raw\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("cli", nargs="?", help="CLI to crawl (e.g., git, docker)")
    parser.add_argument("--config", "-c", type=Path, help="Path to config YAML")
    parser.add_argument("--output", "-o", type=Path, help="Output file path")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./output"),
        help="Output directory (default: ./output)",
    )
    parser.add_argument("--all", action="store_true", help="Crawl all CLIs in config")
    parser.add_argument(
        "--include-raw", action="store_true", help="Include raw help text in main JSON"
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    parser.add_argument("--strict", action="store_true", help="Fail on first parse error")
    parser.add_argument("--max-depth", type=int, help="Override max recursion depth")
    parser.add_argument("--timeout", type=int, help="Override timeout per command (seconds)")
    parser.add_argument("--list", action="store_true", help="List configured CLIs and exit")

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # Load config
    config: CrawlerConfig
    if args.config and args.config.exists():
        config = load_config(str(args.config))
    else:
        config = CrawlerConfig()

    # List mode
    if args.list:
        if not config.clis:
            print("No CLIs configured. Use --config to specify a config file.")
        else:
            print(f"Configured CLIs ({len(config.clis)}):")
            for name, cfg in sorted(config.clis.items()):
                group = f" [{cfg.group}]" if cfg.group else ""
                env = f" (env: {cfg.environment})" if cfg.environment != "wsl" else ""
                print(f"  {name}{group}{env}")
        return

    # Crawl all CLIs
    if args.all:
        if not config.clis:
            print("No CLIs configured. Use --config to specify a config file.")
            sys.exit(1)
        crawl_all(config, args.output_dir, args.include_raw, args.strict)
        return

    # Crawl single CLI
    if args.cli:
        cli_config = config.clis.get(args.cli, CLIConfig(name=args.cli))

        # Apply CLI arg overrides
        if args.max_depth is not None:
            cli_config.max_depth = args.max_depth
        if args.timeout is not None:
            cli_config.timeout = args.timeout

        output = args.output or args.output_dir / f"{args.cli}.json"
        crawl_cli(args.cli, cli_config, output, args.include_raw, args.strict)
        return

    # No action specified
    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
