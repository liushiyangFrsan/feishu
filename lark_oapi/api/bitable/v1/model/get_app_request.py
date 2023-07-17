# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetAppRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None

    @staticmethod
    def builder() -> "GetAppRequestBuilder":
        return GetAppRequestBuilder()


class GetAppRequestBuilder(object):

    def __init__(self, get_app_request: GetAppRequest = GetAppRequest()) -> None:
        get_app_request.http_method = HttpMethod.GET
        get_app_request.uri = "/open-apis/bitable/v1/apps/:app_token"
        get_app_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_app_request: GetAppRequest = get_app_request

    def app_token(self, app_token: str) -> "GetAppRequestBuilder":
        self._get_app_request.app_token = app_token
        self._get_app_request.paths["app_token"] = app_token
        return self

    def build(self) -> GetAppRequest:
        return self._get_app_request
