from http.client import NOT_FOUND
import logging
import sys

import requests

from filename_suggestion_ai.config import (
    MODEL,
    SYSTEM_CONTENT,
)
from filename_suggestion_ai.models import LMStudioChatResponse


class APIClient:
    def __init__(self, url: str, headers: dict) -> None:
        self.url = url
        self.headers = headers

    def send_post_request(self, payload):
        try:
            response = requests.post(self.url, json=payload, headers=self.headers, timeout=60)
            if response.status_code == NOT_FOUND:
                logging.error("Resource not found at %s", self.url)
                sys.exit(1)
            response.raise_for_status()
            return LMStudioChatResponse(**response.json())
        except requests.exceptions.HTTPError:
            logging.exception("HTTP error occurred")
        except requests.exceptions.RequestException:
            logging.exception("Error during requests to %s", self.url)
        except Exception:
            logging.exception("An unexpected error occurred")
            raise
        return None

    def create_payload(self, user_content: str) -> dict:
        """Create the payload for the POST request using the user content.

        Args:
            user_content (str): The content provided by the user.

        Returns:
            dict: The payload dictionary configured for the request.
        """
        return {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_CONTENT},
                {"role": "user", "content": user_content},
            ],
            "temperature": 0.8,
            "max_tokens": -1,
            "seed": -1,
            "stream": False,
        }
