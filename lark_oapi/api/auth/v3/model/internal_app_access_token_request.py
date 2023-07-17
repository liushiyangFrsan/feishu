# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod
from lark_oapi.core.model import BaseRequest
from .internal_app_access_token_request_body import InternalAppAccessTokenRequestBody


class InternalAppAccessTokenRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[InternalAppAccessTokenRequestBody] = None

    @staticmethod
    def builder() -> "InternalAppAccessTokenRequestBuilder":
        return InternalAppAccessTokenRequestBuilder()


class InternalAppAccessTokenRequestBuilder(object):

    def __init__(self,
                 internal_app_access_token_request: InternalAppAccessTokenRequest = InternalAppAccessTokenRequest()) -> None:
        internal_app_access_token_request.http_method = HttpMethod.POST
        internal_app_access_token_request.uri = "/open-apis/auth/v3/app_access_token/internal"
        internal_app_access_token_request.token_types = {}
        self._internal_app_access_token_request: InternalAppAccessTokenRequest = internal_app_access_token_request

    def request_body(self, request_body: InternalAppAccessTokenRequestBody) -> "InternalAppAccessTokenRequestBuilder":
        self._internal_app_access_token_request.request_body = request_body
        self._internal_app_access_token_request.body = request_body
        return self

    def build(self) -> InternalAppAccessTokenRequest:
        return self._internal_app_access_token_request
