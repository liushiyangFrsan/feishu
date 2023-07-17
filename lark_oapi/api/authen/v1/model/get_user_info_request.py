# Code generated by Lark OpenAPI.

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetUserInfoRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "GetUserInfoRequestBuilder":
        return GetUserInfoRequestBuilder()


class GetUserInfoRequestBuilder(object):

    def __init__(self, get_user_info_request: GetUserInfoRequest = GetUserInfoRequest()) -> None:
        get_user_info_request.http_method = HttpMethod.GET
        get_user_info_request.uri = "/open-apis/authen/v1/user_info"
        get_user_info_request.token_types = {AccessTokenType.USER}
        self._get_user_info_request: GetUserInfoRequest = get_user_info_request

    def build(self) -> GetUserInfoRequest:
        return self._get_user_info_request
