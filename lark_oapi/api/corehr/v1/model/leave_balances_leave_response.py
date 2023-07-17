# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .leave_balances_leave_response_body import LeaveBalancesLeaveResponseBody


class LeaveBalancesLeaveResponse(BaseResponse):
    _types = {
        "data": LeaveBalancesLeaveResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[LeaveBalancesLeaveResponseBody] = None
        init(self, d, self._types)
