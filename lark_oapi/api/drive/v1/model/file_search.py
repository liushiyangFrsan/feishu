# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FileSearch(object):
    _types = {
        "docs_token": str,
        "docs_type": str,
        "title": str,
        "owner_id": str,
    }

    def __init__(self, d):
        self.docs_token: Optional[str] = None
        self.docs_type: Optional[str] = None
        self.title: Optional[str] = None
        self.owner_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileSearchBuilder":
        return FileSearchBuilder()


class FileSearchBuilder(object):
    def __init__(self, file_search: FileSearch = FileSearch({})) -> None:
        self._file_search: FileSearch = file_search

    def docs_token(self, docs_token: str) -> "FileSearchBuilder":
        self._file_search.docs_token = docs_token
        return self

    def docs_type(self, docs_type: str) -> "FileSearchBuilder":
        self._file_search.docs_type = docs_type
        return self

    def title(self, title: str) -> "FileSearchBuilder":
        self._file_search.title = title
        return self

    def owner_id(self, owner_id: str) -> "FileSearchBuilder":
        self._file_search.owner_id = owner_id
        return self

    def build(self) -> "FileSearch":
        return self._file_search
