# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_calendar_acl_response_body import CreateCalendarAclResponseBody


class CreateCalendarAclResponse(BaseResponse):
    _types = {
        "data": CreateCalendarAclResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateCalendarAclResponseBody] = None
        init(self, d, self._types)
