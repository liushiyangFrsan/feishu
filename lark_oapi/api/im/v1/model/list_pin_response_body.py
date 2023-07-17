# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .pin import Pin


class ListPinResponseBody(object):
    _types = {
        "items": List[Pin],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[Pin]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListPinResponseBodyBuilder":
        return ListPinResponseBodyBuilder()


class ListPinResponseBodyBuilder(object):
    def __init__(self, list_pin_response_body: ListPinResponseBody = ListPinResponseBody({})) -> None:
        self._list_pin_response_body: ListPinResponseBody = list_pin_response_body

    def items(self, items: List[Pin]) -> "ListPinResponseBodyBuilder":
        self._list_pin_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListPinResponseBodyBuilder":
        self._list_pin_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListPinResponseBodyBuilder":
        self._list_pin_response_body.page_token = page_token
        return self

    def build(self) -> "ListPinResponseBody":
        return self._list_pin_response_body
