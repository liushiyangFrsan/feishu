# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DownloadMediaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.extra: Optional[str] = None
        self.file_token: Optional[str] = None

    @staticmethod
    def builder() -> "DownloadMediaRequestBuilder":
        return DownloadMediaRequestBuilder()


class DownloadMediaRequestBuilder(object):

    def __init__(self, download_media_request: DownloadMediaRequest = DownloadMediaRequest()) -> None:
        download_media_request.http_method = HttpMethod.GET
        download_media_request.uri = "/open-apis/drive/v1/medias/:file_token/download"
        download_media_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._download_media_request: DownloadMediaRequest = download_media_request

    def extra(self, extra: str) -> "DownloadMediaRequestBuilder":
        self._download_media_request.extra = extra
        self._download_media_request.queries["extra"] = str(extra)
        return self

    def file_token(self, file_token: str) -> "DownloadMediaRequestBuilder":
        self._download_media_request.file_token = file_token
        self._download_media_request.paths["file_token"] = file_token
        return self

    def build(self) -> DownloadMediaRequest:
        return self._download_media_request
