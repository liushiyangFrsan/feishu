# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetUserRequestBuilder":
        return GetUserRequestBuilder()


class GetUserRequestBuilder(object):

    def __init__(self, get_user_request: GetUserRequest = GetUserRequest()) -> None:
        get_user_request.http_method = HttpMethod.GET
        get_user_request.uri = "/open-apis/acs/v1/users/:user_id"
        get_user_request.token_types = {AccessTokenType.TENANT}
        self._get_user_request: GetUserRequest = get_user_request

    def user_id_type(self, user_id_type: str) -> "GetUserRequestBuilder":
        self._get_user_request.user_id_type = user_id_type
        self._get_user_request.queries["user_id_type"] = str(user_id_type)
        return self

    def user_id(self, user_id: str) -> "GetUserRequestBuilder":
        self._get_user_request.user_id = user_id
        self._get_user_request.paths["user_id"] = user_id
        return self

    def build(self) -> GetUserRequest:
        return self._get_user_request
