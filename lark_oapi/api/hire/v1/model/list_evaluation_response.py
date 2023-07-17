# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_evaluation_response_body import ListEvaluationResponseBody


class ListEvaluationResponse(BaseResponse):
    _types = {
        "data": ListEvaluationResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListEvaluationResponseBody] = None
        init(self, d, self._types)
