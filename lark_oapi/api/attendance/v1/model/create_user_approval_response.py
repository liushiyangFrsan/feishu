# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_user_approval_response_body import CreateUserApprovalResponseBody


class CreateUserApprovalResponse(BaseResponse):
    _types = {
        "data": CreateUserApprovalResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateUserApprovalResponseBody] = None
        init(self, d, self._types)
