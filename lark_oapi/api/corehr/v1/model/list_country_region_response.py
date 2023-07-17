# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_country_region_response_body import ListCountryRegionResponseBody


class ListCountryRegionResponse(BaseResponse):
    _types = {
        "data": ListCountryRegionResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListCountryRegionResponseBody] = None
        init(self, d, self._types)
