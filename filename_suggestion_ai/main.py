from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import requests

from filename_suggestion_ai.config import (
    HEADERS,
    MODEL,
    SYSTEM_CONTENT,
    URL,
    get_parsed_args,
    initialize_application,
)
from filename_suggestion_ai.models import LMStudioChatResponse
from filename_suggestion_ai.utils import read_file_content


def create_payload(user_content: str) -> dict:
    """
    Creates the payload for the POST request using the user content.

    Args:
        user_content (str): The content provided by the user.

    Returns:
        dict: The payload dictionary.
    """
    return {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_CONTENT,
            },
            {
                "role": "user",
                "content": user_content,
            },
        ],
        "temperature": 0.8,
        "max_tokens": -1,
        "seed": -1,
        "stream": False,
    }


def main() -> None:
    args = get_parsed_args()
    initialize_application()

    # Read file content
    user_content = read_file_content(Path(args.file))
    if user_content is None:
        logging.error("Failed to read file content. Exiting.")
        return

    # Create and send payload
    payload = create_payload(user_content)
    response = send_post_request(URL, HEADERS, payload)
    if response is None:
        logging.error("Failed to receive a valid response. Exiting.")
        return
    answer = response["choices"][0]["message"]["content"]

    logging.info("Answer: %s", answer)


def send_post_request(url: str, headers: dict[str, str], payload: dict) -> LMStudioChatResponse | None:
    """
    Send a POST request to the specified URL with the given headers and payload.

    Args:
        url (str): The URL to which the POST request is sent.
        headers (Dict[str, str]): HTTP headers for the request.
        payload (Dict): The JSON payload for the POST request.

    Returns:
        Optional[ChatCompletionResponse]: The parsed chat completion response or None if an error occurs.
    """
    try:
        logging.info(f"Sending POST request to {url}")
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        logging.info("Successfully sent POST request. Status Code: %s", response.status_code)
        logging.debug("Complete response")
        return LMStudioChatResponse(**response.json())
    except requests.exceptions.HTTPError:
        logging.exception("HTTP error occurred")
    except requests.exceptions.RequestException:
        logging.exception("Error during requests to %s", url)
    except Exception:
        logging.exception("An unexpected error occurred")
    return None


if __name__ == "__main__":
    main()
