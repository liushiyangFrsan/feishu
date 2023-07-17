# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_system_status_response_body import ListSystemStatusResponseBody


class ListSystemStatusResponse(BaseResponse):
    _types = {
        "data": ListSystemStatusResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListSystemStatusResponseBody] = None
        init(self, d, self._types)
