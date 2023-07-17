# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_job_level_response_body import GetJobLevelResponseBody


class GetJobLevelResponse(BaseResponse):
    _types = {
        "data": GetJobLevelResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetJobLevelResponseBody] = None
        init(self, d, self._types)
