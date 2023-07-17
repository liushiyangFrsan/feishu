# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListCategoryRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.lang: Optional[str] = None
        self.order_by: Optional[int] = None
        self.asc: Optional[bool] = None

    @staticmethod
    def builder() -> "ListCategoryRequestBuilder":
        return ListCategoryRequestBuilder()


class ListCategoryRequestBuilder(object):

    def __init__(self, list_category_request: ListCategoryRequest = ListCategoryRequest()) -> None:
        list_category_request.http_method = HttpMethod.GET
        list_category_request.uri = "/open-apis/helpdesk/v1/categories"
        list_category_request.token_types = {AccessTokenType.TENANT}
        self._list_category_request: ListCategoryRequest = list_category_request

    def lang(self, lang: str) -> "ListCategoryRequestBuilder":
        self._list_category_request.lang = lang
        self._list_category_request.queries["lang"] = str(lang)
        return self

    def order_by(self, order_by: int) -> "ListCategoryRequestBuilder":
        self._list_category_request.order_by = order_by
        self._list_category_request.queries["order_by"] = str(order_by)
        return self

    def asc(self, asc: bool) -> "ListCategoryRequestBuilder":
        self._list_category_request.asc = asc
        self._list_category_request.queries["asc"] = str(asc)
        return self

    def build(self) -> ListCategoryRequest:
        return self._list_category_request
