# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UploadAllMediaResponseBody(object):
    _types = {
        "file_token": str,
    }

    def __init__(self, d):
        self.file_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadAllMediaResponseBodyBuilder":
        return UploadAllMediaResponseBodyBuilder()


class UploadAllMediaResponseBodyBuilder(object):
    def __init__(self,
                 upload_all_media_response_body: UploadAllMediaResponseBody = UploadAllMediaResponseBody({})) -> None:
        self._upload_all_media_response_body: UploadAllMediaResponseBody = upload_all_media_response_body

    def file_token(self, file_token: str) -> "UploadAllMediaResponseBodyBuilder":
        self._upload_all_media_response_body.file_token = file_token
        return self

    def build(self) -> "UploadAllMediaResponseBody":
        return self._upload_all_media_response_body
