#!/usr/bin/env python3
"""Legacy compatibility script for ``cli-crawler``.

Prefer invoking the canonical command directly:

    cli-crawler <cli_name> [options]
"""

from crawler.cli_crawler import main

if __name__ == "__main__":
    main()
