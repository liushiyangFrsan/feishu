# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .underauditlist_application_response_body import UnderauditlistApplicationResponseBody


class UnderauditlistApplicationResponse(BaseResponse):
    _types = {
        "data": UnderauditlistApplicationResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UnderauditlistApplicationResponseBody] = None
        init(self, d, self._types)
