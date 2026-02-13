"""Unit tests for src/lib/logger.py — T008."""

import logging

import lib.logger as logger_module
from lib.logger import get_logger


def _reset():
    """Reset module-level _configured flag so _configure_root runs again."""
    logger_module._configured = False
    logging.getLogger().handlers.clear()


def test_get_logger_returns_named_logger():
    logger = get_logger("cli_plugins.test")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "cli_plugins.test"


def test_get_logger_default_level_info(monkeypatch):
    monkeypatch.delenv("CLI_PLUGINS_LOG_LEVEL", raising=False)
    _reset()
    get_logger("cli_plugins.info_test")
    assert logging.getLogger().level <= logging.INFO


def test_get_logger_env_var_debug(monkeypatch):
    monkeypatch.setenv("CLI_PLUGINS_LOG_LEVEL", "DEBUG")
    _reset()
    get_logger("cli_plugins.debug_test")
    assert logging.getLogger().level <= logging.DEBUG


def test_get_logger_invalid_level_does_not_raise(monkeypatch):
    monkeypatch.setenv("CLI_PLUGINS_LOG_LEVEL", "NOT_A_LEVEL")
    _reset()
    logger = get_logger("cli_plugins.invalid_test")
    assert isinstance(logger, logging.Logger)


def test_get_logger_same_name_returns_same_instance():
    a = get_logger("cli_plugins.singleton")
    b = get_logger("cli_plugins.singleton")
    assert a is b
