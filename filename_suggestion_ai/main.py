from __future__ import annotations

from pathlib import Path

from filename_suggestion_ai.config import (
    get_parsed_args,
    initialize_application,
)
from filename_suggestion_ai.modules import FileProcessor


def main():
    args = get_parsed_args()
    initialize_application()
    processor = FileProcessor(
        directory=Path(args.directory) if args.directory else None,
        file=Path(args.file) if args.file else None,
        filter_ext=args.filter,
    )
    processor.process_files()


if __name__ == "__main__":
    main()
