# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_folder_file_request_body import CreateFolderFileRequestBody


class CreateFolderFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateFolderFileRequestBody] = None

    @staticmethod
    def builder() -> "CreateFolderFileRequestBuilder":
        return CreateFolderFileRequestBuilder()


class CreateFolderFileRequestBuilder(object):

    def __init__(self, create_folder_file_request: CreateFolderFileRequest = CreateFolderFileRequest()) -> None:
        create_folder_file_request.http_method = HttpMethod.POST
        create_folder_file_request.uri = "/open-apis/drive/v1/files/create_folder"
        create_folder_file_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_folder_file_request: CreateFolderFileRequest = create_folder_file_request

    def request_body(self, request_body: CreateFolderFileRequestBody) -> "CreateFolderFileRequestBuilder":
        self._create_folder_file_request.request_body = request_body
        self._create_folder_file_request.body = request_body
        return self

    def build(self) -> CreateFolderFileRequest:
        return self._create_folder_file_request
