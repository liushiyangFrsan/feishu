# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateFolderFileResponseBody(object):
    _types = {
        "token": str,
        "url": str,
    }

    def __init__(self, d):
        self.token: Optional[str] = None
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateFolderFileResponseBodyBuilder":
        return CreateFolderFileResponseBodyBuilder()


class CreateFolderFileResponseBodyBuilder(object):
    def __init__(self, create_folder_file_response_body: CreateFolderFileResponseBody = CreateFolderFileResponseBody(
        {})) -> None:
        self._create_folder_file_response_body: CreateFolderFileResponseBody = create_folder_file_response_body

    def token(self, token: str) -> "CreateFolderFileResponseBodyBuilder":
        self._create_folder_file_response_body.token = token
        return self

    def url(self, url: str) -> "CreateFolderFileResponseBodyBuilder":
        self._create_folder_file_response_body.url = url
        return self

    def build(self) -> "CreateFolderFileResponseBody":
        return self._create_folder_file_response_body