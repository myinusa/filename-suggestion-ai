from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import requests
from tqdm import tqdm

from filename_suggestion_ai.config import (
    HEADERS,
    URL,
    get_parsed_args,
    initialize_application,
)
from filename_suggestion_ai.utils import APIClient, read_file_content


def main() -> None:
    args = get_parsed_args()
    initialize_application()

    if args.directory:
        directory_path = Path(args.directory)
        answers = []
        if args.filter:
            files = [
                file_path
                for file_path in directory_path.iterdir()
                if file_path.is_file() and file_path.suffix == args.filter
            ]
        else:
            files = [file_path for file_path in directory_path.iterdir() if file_path.is_file()]
        logging.info(f"Total number of files in directory: {len(files)}")
        for file_path in tqdm(files, desc="Processing files"):
            answer = process_file(file_path)
            if answer:
                answers.append((file_path, answer))
        for f_file_path, answer in answers:
            file = f_file_path.name
            logging.info(f"{file:20} | {answer}")
    elif args.file:
        file_path = Path(args.file)
        answer = process_file(file_path)
        if answer:
            logging.info(f"Answer for {file_path}: {answer}")
    else:
        logging.error("No file or directory specified. Exiting.")
        return


def process_file(file_path: Path):
    user_content = read_file_content(file_path)
    if user_content is None:
        logging.error(f"Failed to read file content from {file_path}. Skipping.")
        return None

    client = APIClient(URL, HEADERS)
    payload = client.create_payload(user_content)
    response = client.send_post_request(payload)
    if response is None:
        logging.error("Failed to receive a valid response. Exiting.")
        return None
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    main()
