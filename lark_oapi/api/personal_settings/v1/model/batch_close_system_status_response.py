# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_close_system_status_response_body import BatchCloseSystemStatusResponseBody


class BatchCloseSystemStatusResponse(BaseResponse):
    _types = {
        "data": BatchCloseSystemStatusResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[BatchCloseSystemStatusResponseBody] = None
        init(self, d, self._types)
