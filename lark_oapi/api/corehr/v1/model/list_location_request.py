# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListLocationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListLocationRequestBuilder":
        return ListLocationRequestBuilder()


class ListLocationRequestBuilder(object):

    def __init__(self, list_location_request: ListLocationRequest = ListLocationRequest()) -> None:
        list_location_request.http_method = HttpMethod.GET
        list_location_request.uri = "/open-apis/corehr/v1/locations"
        list_location_request.token_types = {AccessTokenType.TENANT}
        self._list_location_request: ListLocationRequest = list_location_request

    def page_token(self, page_token: str) -> "ListLocationRequestBuilder":
        self._list_location_request.page_token = page_token
        self._list_location_request.queries["page_token"] = str(page_token)
        return self

    def page_size(self, page_size: str) -> "ListLocationRequestBuilder":
        self._list_location_request.page_size = page_size
        self._list_location_request.queries["page_size"] = str(page_size)
        return self

    def build(self) -> ListLocationRequest:
        return self._list_location_request
