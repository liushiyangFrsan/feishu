# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_folder import TalentFolder


class ListTalentFolderResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[TalentFolder],
    }

    def __init__(self, d):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[TalentFolder]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTalentFolderResponseBodyBuilder":
        return ListTalentFolderResponseBodyBuilder()


class ListTalentFolderResponseBodyBuilder(object):
    def __init__(self, list_talent_folder_response_body: ListTalentFolderResponseBody = ListTalentFolderResponseBody(
        {})) -> None:
        self._list_talent_folder_response_body: ListTalentFolderResponseBody = list_talent_folder_response_body

    def has_more(self, has_more: bool) -> "ListTalentFolderResponseBodyBuilder":
        self._list_talent_folder_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListTalentFolderResponseBodyBuilder":
        self._list_talent_folder_response_body.page_token = page_token
        return self

    def items(self, items: List[TalentFolder]) -> "ListTalentFolderResponseBodyBuilder":
        self._list_talent_folder_response_body.items = items
        return self

    def build(self) -> "ListTalentFolderResponseBody":
        return self._list_talent_folder_response_body
