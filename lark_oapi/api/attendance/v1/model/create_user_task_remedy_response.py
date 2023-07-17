# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_user_task_remedy_response_body import CreateUserTaskRemedyResponseBody


class CreateUserTaskRemedyResponse(BaseResponse):
    _types = {
        "data": CreateUserTaskRemedyResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateUserTaskRemedyResponseBody] = None
        init(self, d, self._types)
