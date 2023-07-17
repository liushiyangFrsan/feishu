# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_chat_menu_tree_request_body import CreateChatMenuTreeRequestBody


class CreateChatMenuTreeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None
        self.request_body: Optional[CreateChatMenuTreeRequestBody] = None

    @staticmethod
    def builder() -> "CreateChatMenuTreeRequestBuilder":
        return CreateChatMenuTreeRequestBuilder()


class CreateChatMenuTreeRequestBuilder(object):

    def __init__(self, create_chat_menu_tree_request: CreateChatMenuTreeRequest = CreateChatMenuTreeRequest()) -> None:
        create_chat_menu_tree_request.http_method = HttpMethod.POST
        create_chat_menu_tree_request.uri = "/open-apis/im/v1/chats/:chat_id/menu_tree"
        create_chat_menu_tree_request.token_types = {AccessTokenType.TENANT}
        self._create_chat_menu_tree_request: CreateChatMenuTreeRequest = create_chat_menu_tree_request

    def chat_id(self, chat_id: str) -> "CreateChatMenuTreeRequestBuilder":
        self._create_chat_menu_tree_request.chat_id = chat_id
        self._create_chat_menu_tree_request.paths["chat_id"] = chat_id
        return self

    def request_body(self, request_body: CreateChatMenuTreeRequestBody) -> "CreateChatMenuTreeRequestBuilder":
        self._create_chat_menu_tree_request.request_body = request_body
        self._create_chat_menu_tree_request.body = request_body
        return self

    def build(self) -> CreateChatMenuTreeRequest:
        return self._create_chat_menu_tree_request
