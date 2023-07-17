# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ReplaceFileRequest(object):
    _types = {
        "token": str,
    }

    def __init__(self, d):
        self.token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReplaceFileRequestBuilder":
        return ReplaceFileRequestBuilder()


class ReplaceFileRequestBuilder(object):
    def __init__(self, replace_file_request: ReplaceFileRequest = ReplaceFileRequest({})) -> None:
        self._replace_file_request: ReplaceFileRequest = replace_file_request

    def token(self, token: str) -> "ReplaceFileRequestBuilder":
        self._replace_file_request.token = token
        return self

    def build(self) -> "ReplaceFileRequest":
        return self._replace_file_request
