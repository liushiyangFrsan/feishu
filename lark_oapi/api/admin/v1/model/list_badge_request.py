# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListBadgeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.name: Optional[str] = None

    @staticmethod
    def builder() -> "ListBadgeRequestBuilder":
        return ListBadgeRequestBuilder()


class ListBadgeRequestBuilder(object):

    def __init__(self, list_badge_request: ListBadgeRequest = ListBadgeRequest()) -> None:
        list_badge_request.http_method = HttpMethod.GET
        list_badge_request.uri = "/open-apis/admin/v1/badges"
        list_badge_request.token_types = {AccessTokenType.TENANT}
        self._list_badge_request: ListBadgeRequest = list_badge_request

    def page_size(self, page_size: int) -> "ListBadgeRequestBuilder":
        self._list_badge_request.page_size = page_size
        self._list_badge_request.queries["page_size"] = str(page_size)
        return self

    def page_token(self, page_token: str) -> "ListBadgeRequestBuilder":
        self._list_badge_request.page_token = page_token
        self._list_badge_request.queries["page_token"] = str(page_token)
        return self

    def name(self, name: str) -> "ListBadgeRequestBuilder":
        self._list_badge_request.name = name
        self._list_badge_request.queries["name"] = str(name)
        return self

    def build(self) -> ListBadgeRequest:
        return self._list_badge_request
