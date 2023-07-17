# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_user_task_response_body import QueryUserTaskResponseBody


class QueryUserTaskResponse(BaseResponse):
    _types = {
        "data": QueryUserTaskResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[QueryUserTaskResponseBody] = None
        init(self, d, self._types)
