# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .chat_menu_item import ChatMenuItem


class PatchChatMenuItemResponseBody(object):
    _types = {
        "chat_menu_item": ChatMenuItem,
    }

    def __init__(self, d):
        self.chat_menu_item: Optional[ChatMenuItem] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchChatMenuItemResponseBodyBuilder":
        return PatchChatMenuItemResponseBodyBuilder()


class PatchChatMenuItemResponseBodyBuilder(object):
    def __init__(self,
                 patch_chat_menu_item_response_body: PatchChatMenuItemResponseBody = PatchChatMenuItemResponseBody(
                     {})) -> None:
        self._patch_chat_menu_item_response_body: PatchChatMenuItemResponseBody = patch_chat_menu_item_response_body

    def chat_menu_item(self, chat_menu_item: ChatMenuItem) -> "PatchChatMenuItemResponseBodyBuilder":
        self._patch_chat_menu_item_response_body.chat_menu_item = chat_menu_item
        return self

    def build(self) -> "PatchChatMenuItemResponseBody":
        return self._patch_chat_menu_item_response_body
