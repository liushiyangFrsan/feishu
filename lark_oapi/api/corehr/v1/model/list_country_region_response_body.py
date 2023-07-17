# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .country_region import CountryRegion


class ListCountryRegionResponseBody(object):
    _types = {
        "items": List[CountryRegion],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[CountryRegion]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListCountryRegionResponseBodyBuilder":
        return ListCountryRegionResponseBodyBuilder()


class ListCountryRegionResponseBodyBuilder(object):
    def __init__(self, list_country_region_response_body: ListCountryRegionResponseBody = ListCountryRegionResponseBody(
        {})) -> None:
        self._list_country_region_response_body: ListCountryRegionResponseBody = list_country_region_response_body

    def items(self, items: List[CountryRegion]) -> "ListCountryRegionResponseBodyBuilder":
        self._list_country_region_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListCountryRegionResponseBodyBuilder":
        self._list_country_region_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListCountryRegionResponseBodyBuilder":
        self._list_country_region_response_body.page_token = page_token
        return self

    def build(self) -> "ListCountryRegionResponseBody":
        return self._list_country_region_response_body
