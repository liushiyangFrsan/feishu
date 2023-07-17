# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .urgent_phone_message_response_body import UrgentPhoneMessageResponseBody


class UrgentPhoneMessageResponse(BaseResponse):
    _types = {
        "data": UrgentPhoneMessageResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UrgentPhoneMessageResponseBody] = None
        init(self, d, self._types)
