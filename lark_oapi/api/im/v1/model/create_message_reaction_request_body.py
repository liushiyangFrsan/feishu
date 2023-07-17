# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .emoji import Emoji


class CreateMessageReactionRequestBody(object):
    _types = {
        "reaction_type": Emoji,
    }

    def __init__(self, d):
        self.reaction_type: Optional[Emoji] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMessageReactionRequestBodyBuilder":
        return CreateMessageReactionRequestBodyBuilder()


class CreateMessageReactionRequestBodyBuilder(object):
    def __init__(self,
                 create_message_reaction_request_body: CreateMessageReactionRequestBody = CreateMessageReactionRequestBody(
                     {})) -> None:
        self._create_message_reaction_request_body: CreateMessageReactionRequestBody = create_message_reaction_request_body

    def reaction_type(self, reaction_type: Emoji) -> "CreateMessageReactionRequestBodyBuilder":
        self._create_message_reaction_request_body.reaction_type = reaction_type
        return self

    def build(self) -> "CreateMessageReactionRequestBody":
        return self._create_message_reaction_request_body
