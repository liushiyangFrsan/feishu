# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetChatMenuTreeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetChatMenuTreeRequestBuilder":
        return GetChatMenuTreeRequestBuilder()


class GetChatMenuTreeRequestBuilder(object):

    def __init__(self, get_chat_menu_tree_request: GetChatMenuTreeRequest = GetChatMenuTreeRequest()) -> None:
        get_chat_menu_tree_request.http_method = HttpMethod.GET
        get_chat_menu_tree_request.uri = "/open-apis/im/v1/chats/:chat_id/menu_tree"
        get_chat_menu_tree_request.token_types = {AccessTokenType.TENANT}
        self._get_chat_menu_tree_request: GetChatMenuTreeRequest = get_chat_menu_tree_request

    def chat_id(self, chat_id: str) -> "GetChatMenuTreeRequestBuilder":
        self._get_chat_menu_tree_request.chat_id = chat_id
        self._get_chat_menu_tree_request.paths["chat_id"] = chat_id
        return self

    def build(self) -> GetChatMenuTreeRequest:
        return self._get_chat_menu_tree_request
