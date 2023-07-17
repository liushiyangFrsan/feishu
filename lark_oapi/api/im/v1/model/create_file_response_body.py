# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateFileResponseBody(object):
    _types = {
        "file_key": str,
    }

    def __init__(self, d):
        self.file_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateFileResponseBodyBuilder":
        return CreateFileResponseBodyBuilder()


class CreateFileResponseBodyBuilder(object):
    def __init__(self, create_file_response_body: CreateFileResponseBody = CreateFileResponseBody({})) -> None:
        self._create_file_response_body: CreateFileResponseBody = create_file_response_body

    def file_key(self, file_key: str) -> "CreateFileResponseBodyBuilder":
        self._create_file_response_body.file_key = file_key
        return self

    def build(self) -> "CreateFileResponseBody":
        return self._create_file_response_body
