from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING

from tqdm import tqdm

from filename_suggestion_ai.config import HEADERS, URL
from filename_suggestion_ai.utils import APIClient, read_file_content

if TYPE_CHECKING:
    from filename_suggestion_ai.models import LMStudioChatResponse


class FileProcessor:
    def __init__(self, directory: Path | None, file: Path | None, filter_ext: str) -> None:
        self.directory = directory
        self.file = file
        self.filter_ext = filter_ext
        self.client = APIClient(URL, HEADERS)

    def process_files(self):
        if self.directory:
            return self._process_directory()
        elif self.file:
            return self._process_single_file()
        else:
            logging.error("No file or directory specified. Exiting.")
            return None

    def _process_directory(self):
        if not isinstance(self.directory, Path):
            logging.error("Invalid directory path specified. Exiting.")
            return None
        files = [
            f
            for f in self.directory.iterdir()
            if f.is_file() and (self.filter_ext is None or f.suffix == self.filter_ext)
        ]
        logging.info(f"Total number of files in directory: {len(files)}")
        answers = []
        for file_path in tqdm(files, desc="Processing files"):
            answer = self._process_file(file_path)
            if answer:
                answers.append((file_path.name, answer))
        for name, answer in answers:
            logging.info(f"{name:20} | {answer}")
        return answers

    def _process_single_file(self):
        if not isinstance(self.file, Path):
            logging.error("Invalid file path specified. Exiting.")
            return None
        answer = self._process_file(self.file)
        if answer:
            logging.info(f"Answer for {self.file}: {answer}")
        return [(self.file.name, answer)]

    def _process_file(self, file_path: Path) -> LMStudioChatResponse | None:
        # if file_path.suffix in {".toml", ""} or file_path.suffix.startswith("."):
            # logging.info(f"Skipping file {file_path} due to unwanted extension.")
            # return None
        if file_path.stat().st_size > 100 * 1024:
            logging.info(f"Skipping file {file_path} as it exceeds 100KB.")
            return None
        content = read_file_content(file_path)
        if content is None:
            return None
        payload = self.client.create_payload(content)
        response = self.client.send_post_request(payload)
        if response:
            return response["choices"][0]["message"]["content"]
        return None
