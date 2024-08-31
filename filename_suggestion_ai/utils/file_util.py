from __future__ import annotations

import logging
from pathlib import Path


def read_file_content(file_path: Path) -> str | None:
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (Path): The path to the file to be read.

    Returns:
        Optional[str]: The content of the file as a string, or None if an error occurs.
    """
    try:
        with file_path.open("r") as file:
            return file.read().replace("\n", "\\n")
    except FileNotFoundError:
        logging.exception("File not found: %s", file_path)
    except OSError as e:
        logging.exception(f"I/O error({e.errno}): {e.strerror}")
    except Exception:
        logging.exception("An unexpected error occurred while reading the file")
    return None
