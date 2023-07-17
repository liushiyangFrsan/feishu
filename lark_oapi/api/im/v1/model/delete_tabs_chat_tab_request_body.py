# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DeleteTabsChatTabRequestBody(object):
    _types = {
        "tab_ids": List[str],
    }

    def __init__(self, d):
        self.tab_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteTabsChatTabRequestBodyBuilder":
        return DeleteTabsChatTabRequestBodyBuilder()


class DeleteTabsChatTabRequestBodyBuilder(object):
    def __init__(self, delete_tabs_chat_tab_request_body: DeleteTabsChatTabRequestBody = DeleteTabsChatTabRequestBody(
        {})) -> None:
        self._delete_tabs_chat_tab_request_body: DeleteTabsChatTabRequestBody = delete_tabs_chat_tab_request_body

    def tab_ids(self, tab_ids: List[str]) -> "DeleteTabsChatTabRequestBodyBuilder":
        self._delete_tabs_chat_tab_request_body.tab_ids = tab_ids
        return self

    def build(self) -> "DeleteTabsChatTabRequestBody":
        return self._delete_tabs_chat_tab_request_body
