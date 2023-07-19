# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_top_user_report_response_body import GetTopUserReportResponseBody


class GetTopUserReportResponse(BaseResponse):
    _types = {
        "data": GetTopUserReportResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetTopUserReportResponseBody] = None
        init(self, d, self._types)