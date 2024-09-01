import logging
from logging.config import dictConfig
from pathlib import Path

from rich.logging import RichHandler
from rich.traceback import install as install_rich_traceback


def setup_logging(log_file: Path, log_level: int = logging.INFO) -> None:
    """Sets up logging configuration."""
    install_rich_traceback()  # Install rich traceback handling
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(levelname)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
                "generic": {
                    "format": "%(asctime)s %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                    "class": "logging.Formatter",
                },
            },
            "handlers": {
                "fileHandler": {
                    "class": "logging.FileHandler",
                    "filename": log_file,
                    "formatter": "default",
                    "level": "DEBUG",  # Always log everything to file
                },
                "console": {
                    "class": "rich.logging.RichHandler",
                    "formatter": "generic",
                    "level": log_level,  # Dynamic log level
                    "rich_tracebacks": True,
                },
            },
            "root": {"level": log_level, "handlers": ["fileHandler", "console"]},
        },
    )
