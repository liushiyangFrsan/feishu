# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_message_reaction_request_body import CreateMessageReactionRequestBody


class CreateMessageReactionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.message_id: Optional[str] = None
        self.request_body: Optional[CreateMessageReactionRequestBody] = None

    @staticmethod
    def builder() -> "CreateMessageReactionRequestBuilder":
        return CreateMessageReactionRequestBuilder()


class CreateMessageReactionRequestBuilder(object):

    def __init__(self,
                 create_message_reaction_request: CreateMessageReactionRequest = CreateMessageReactionRequest()) -> None:
        create_message_reaction_request.http_method = HttpMethod.POST
        create_message_reaction_request.uri = "/open-apis/im/v1/messages/:message_id/reactions"
        create_message_reaction_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_message_reaction_request: CreateMessageReactionRequest = create_message_reaction_request

    def message_id(self, message_id: str) -> "CreateMessageReactionRequestBuilder":
        self._create_message_reaction_request.message_id = message_id
        self._create_message_reaction_request.paths["message_id"] = message_id
        return self

    def request_body(self, request_body: CreateMessageReactionRequestBody) -> "CreateMessageReactionRequestBuilder":
        self._create_message_reaction_request.request_body = request_body
        self._create_message_reaction_request.body = request_body
        return self

    def build(self) -> CreateMessageReactionRequest:
        return self._create_message_reaction_request
