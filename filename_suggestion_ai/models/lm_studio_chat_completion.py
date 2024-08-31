from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Message:
    role: str
    content: str


@dataclass
class Choice:
    index: int
    message: Message
    finish_reason: str
    logprobs: dict | None = None


@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class LMStudioChatResponse:
    """
    LM Studio chat response.

    See https://platform.openai.com/docs/api-reference/chat/create
    See https://lmstudio.ai/docs/local-server
    """

    id: str
    object: str
    created: int
    model: str
    choices: list[Choice]
    usage: Usage
    system_fingerprint: str

    def __getitem__(self, key: str | int) -> LMStudioChatResponse:
        # if isinstance(key, int):
        # Assuming integer keys are for accessing choices list
        # return self.choices[key]
        if isinstance(key, str):
            # String keys for attribute access
            return getattr(self, key)
        else:
            msg = "Key must be either an integer or a string"
            raise TypeError(msg)
