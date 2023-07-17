# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class File(object):
    _types = {
        "token": str,
        "name": str,
        "view_type": int,
    }

    def __init__(self, d):
        self.token: Optional[str] = None
        self.name: Optional[str] = None
        self.view_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileBuilder":
        return FileBuilder()


class FileBuilder(object):
    def __init__(self, file: File = File({})) -> None:
        self._file: File = file

    def token(self, token: str) -> "FileBuilder":
        self._file.token = token
        return self

    def name(self, name: str) -> "FileBuilder":
        self._file.name = name
        return self

    def view_type(self, view_type: int) -> "FileBuilder":
        self._file.view_type = view_type
        return self

    def build(self) -> "File":
        return self._file
