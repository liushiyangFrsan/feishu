# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .district import District


class SearchBasicInfoDistrictResponseBody(object):
    _types = {
        "items": List[District],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[District]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchBasicInfoDistrictResponseBodyBuilder":
        return SearchBasicInfoDistrictResponseBodyBuilder()


class SearchBasicInfoDistrictResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_basic_info_district_response_body = SearchBasicInfoDistrictResponseBody()

    def items(self, items: List[District]) -> "SearchBasicInfoDistrictResponseBodyBuilder":
        self._search_basic_info_district_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchBasicInfoDistrictResponseBodyBuilder":
        self._search_basic_info_district_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchBasicInfoDistrictResponseBodyBuilder":
        self._search_basic_info_district_response_body.has_more = has_more
        return self

    def build(self) -> "SearchBasicInfoDistrictResponseBody":
        return self._search_basic_info_district_response_body