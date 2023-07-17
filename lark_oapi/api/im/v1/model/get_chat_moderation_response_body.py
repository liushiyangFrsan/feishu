# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .list_moderator import ListModerator


class GetChatModerationResponseBody(object):
    _types = {
        "moderation_setting": str,
        "page_token": str,
        "has_more": bool,
        "items": List[ListModerator],
    }

    def __init__(self, d):
        self.moderation_setting: Optional[str] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.items: Optional[List[ListModerator]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetChatModerationResponseBodyBuilder":
        return GetChatModerationResponseBodyBuilder()


class GetChatModerationResponseBodyBuilder(object):
    def __init__(self, get_chat_moderation_response_body: GetChatModerationResponseBody = GetChatModerationResponseBody(
        {})) -> None:
        self._get_chat_moderation_response_body: GetChatModerationResponseBody = get_chat_moderation_response_body

    def moderation_setting(self, moderation_setting: str) -> "GetChatModerationResponseBodyBuilder":
        self._get_chat_moderation_response_body.moderation_setting = moderation_setting
        return self

    def page_token(self, page_token: str) -> "GetChatModerationResponseBodyBuilder":
        self._get_chat_moderation_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "GetChatModerationResponseBodyBuilder":
        self._get_chat_moderation_response_body.has_more = has_more
        return self

    def items(self, items: List[ListModerator]) -> "GetChatModerationResponseBodyBuilder":
        self._get_chat_moderation_response_body.items = items
        return self

    def build(self) -> "GetChatModerationResponseBody":
        return self._get_chat_moderation_response_body
