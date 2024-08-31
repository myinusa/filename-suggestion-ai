import logging

import requests

from filename_suggestion_ai.config import HEADERS, MODEL, SYSTEM_CONTENT, URL, USER_CONTENT, initialize_application

PAYLOAD = {
    "model": MODEL,
    "messages": [
        {
            "role": "system",
            "content": SYSTEM_CONTENT,
        },
        {
            "role": "user",
            "content": USER_CONTENT,
        },
    ],
    "temperature": 0.8,
    "max_tokens": -1,
    "seed": -1,
    "stream": False,
}


def main() -> None:
    initialize_application()
    send_post_request(URL, HEADERS, PAYLOAD)


def send_post_request(url: str, headers: dict[str, str], payload: dict) -> None:
    """
    Send a POST request to the specified URL with the given headers and payload.

    Args:
        url (str): The URL to which the POST request is sent.
        headers (Dict[str, str]): HTTP headers for the request.
        payload (Dict): The JSON payload for the POST request.

    Returns:
        None
    """
    try:
        logging.info("Sending POST request to %s", url)
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        logging.info("Successfully sent POST request. Status Code: %s", response.status_code)
        logging.info("Response Content: %s", response.text)
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error occurred: %s", e)
    except requests.exceptions.RequestException as e:
        logging.error("Error during requests to %s: %s", url, e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)


if __name__ == "__main__":
    main()
