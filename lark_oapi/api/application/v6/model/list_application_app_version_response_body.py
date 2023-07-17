# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_app_version import ApplicationAppVersion


class ListApplicationAppVersionResponseBody(object):
    _types = {
        "items": List[ApplicationAppVersion],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d):
        self.items: Optional[List[ApplicationAppVersion]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListApplicationAppVersionResponseBodyBuilder":
        return ListApplicationAppVersionResponseBodyBuilder()


class ListApplicationAppVersionResponseBodyBuilder(object):
    def __init__(self,
                 list_application_app_version_response_body: ListApplicationAppVersionResponseBody = ListApplicationAppVersionResponseBody(
                     {})) -> None:
        self._list_application_app_version_response_body: ListApplicationAppVersionResponseBody = list_application_app_version_response_body

    def items(self, items: List[ApplicationAppVersion]) -> "ListApplicationAppVersionResponseBodyBuilder":
        self._list_application_app_version_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListApplicationAppVersionResponseBodyBuilder":
        self._list_application_app_version_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListApplicationAppVersionResponseBodyBuilder":
        self._list_application_app_version_response_body.has_more = has_more
        return self

    def build(self) -> "ListApplicationAppVersionResponseBody":
        return self._list_application_app_version_response_body
