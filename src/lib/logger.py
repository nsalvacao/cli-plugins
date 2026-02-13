"""Stdlib-only logging setup for cli-plugins.

All modules should obtain their logger via :func:`get_logger` rather than
calling ``logging.getLogger`` directly, so that formatting and level
configuration stays consistent across the project.

Configuration is driven exclusively by the ``CLI_PLUGINS_LOG_LEVEL``
environment variable (default: ``INFO``).  No external packages are used.
"""

from __future__ import annotations

import logging
import os

_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
_DEFAULT_LEVEL = "INFO"
_configured = False


def get_logger(name: str) -> logging.Logger:
    """Return a named :class:`logging.Logger`, initialising root config on first call.

    Args:
        name: Dot-separated logger hierarchy (e.g. ``"cli_plugins.crawler"``).

    Returns:
        Configured :class:`logging.Logger` instance.
    """
    global _configured  # noqa: PLW0603
    if not _configured:
        _configure_root()
        _configured = True
    return logging.getLogger(name)


def _configure_root() -> None:
    """Configure the root logger from ``CLI_PLUGINS_LOG_LEVEL`` env var.

    Called at most once per process.  Idempotent when root already has handlers
    (e.g. when running under pytest with log capture enabled).
    """
    level_name = os.environ.get("CLI_PLUGINS_LOG_LEVEL", _DEFAULT_LEVEL).upper()
    level = getattr(logging, level_name, logging.INFO)

    root = logging.getLogger()
    if not root.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(_LOG_FORMAT, datefmt=_DATE_FORMAT))
        root.addHandler(handler)

    root.setLevel(level)
