# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetSpaceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.space_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetSpaceRequestBuilder":
        return GetSpaceRequestBuilder()


class GetSpaceRequestBuilder(object):

    def __init__(self, get_space_request: GetSpaceRequest = GetSpaceRequest()) -> None:
        get_space_request.http_method = HttpMethod.GET
        get_space_request.uri = "/open-apis/wiki/v2/spaces/:space_id"
        get_space_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_space_request: GetSpaceRequest = get_space_request

    def space_id(self, space_id: str) -> "GetSpaceRequestBuilder":
        self._get_space_request.space_id = space_id
        self._get_space_request.paths["space_id"] = space_id
        return self

    def build(self) -> GetSpaceRequest:
        return self._get_space_request
