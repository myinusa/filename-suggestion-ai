from datetime import datetime
import logging
import os
from pathlib import Path
import sys

from dotenv import load_dotenv

from .args import get_parsed_args
from .setup_logging import setup_logging

LOG_FILE = "main.log"
LOG_PATH = Path("logs")
LOG_PATH.mkdir(parents=True, exist_ok=True)
LOG_PATH = LOG_PATH / LOG_FILE

load_dotenv()
MAIN_URL = os.getenv("MAIN_URL", "")
# Date format
ISO_DATE_FORMAT = "%y%m%dT%H:%M"


def ensure_directory_exists(path: Path) -> None:
    """Ensure that the directory for the given path exists, exit otherwise."""
    if not path.exists():
        logging.critical(f"Directory {path.resolve()} does not exist.")
        sys.exit(1)


def get_current_date_formatted(_format: str) -> str:
    """Return the current date formatted according to the given format string."""
    return datetime.now().strftime(_format)


def initialize_application() -> None:
    """Initialize application by setting up environment, logging and ensuring directory structure."""
    # load_environment_variables()
    args = get_parsed_args()  # Parse command line arguments

    # Determine the log level based on command line arguments
    if args.debug:
        log_level = logging.DEBUG
    elif args.verbose:
        log_level = logging.INFO
    else:
        log_level = logging.INFO

    setup_logging(LOG_PATH, log_level)
    logging.debug("Initializing application...")
    logging.debug("Application initialized.")


current_date = get_current_date_formatted(ISO_DATE_FORMAT)
