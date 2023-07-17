# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_workplace_access_data_response_body import SearchWorkplaceAccessDataResponseBody


class SearchWorkplaceAccessDataResponse(BaseResponse):
    _types = {
        "data": SearchWorkplaceAccessDataResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[SearchWorkplaceAccessDataResponseBody] = None
        init(self, d, self._types)
