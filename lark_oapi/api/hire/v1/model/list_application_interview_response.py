# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_application_interview_response_body import ListApplicationInterviewResponseBody


class ListApplicationInterviewResponse(BaseResponse):
    _types = {
        "data": ListApplicationInterviewResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListApplicationInterviewResponseBody] = None
        init(self, d, self._types)
