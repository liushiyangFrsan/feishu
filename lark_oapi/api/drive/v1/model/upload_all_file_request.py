# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .upload_all_file_request_body import UploadAllFileRequestBody


class UploadAllFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[UploadAllFileRequestBody] = None

    @staticmethod
    def builder() -> "UploadAllFileRequestBuilder":
        return UploadAllFileRequestBuilder()


class UploadAllFileRequestBuilder(object):

    def __init__(self, upload_all_file_request: UploadAllFileRequest = UploadAllFileRequest()) -> None:
        upload_all_file_request.http_method = HttpMethod.POST
        upload_all_file_request.uri = "/open-apis/drive/v1/files/upload_all"
        upload_all_file_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._upload_all_file_request: UploadAllFileRequest = upload_all_file_request

    def request_body(self, request_body: UploadAllFileRequestBody) -> "UploadAllFileRequestBuilder":
        self._upload_all_file_request.request_body = request_body
        self._upload_all_file_request.body = request_body
        return self

    def build(self) -> UploadAllFileRequest:
        return self._upload_all_file_request
