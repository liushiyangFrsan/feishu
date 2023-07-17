# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_working_hours_type_response_body import CreateWorkingHoursTypeResponseBody


class CreateWorkingHoursTypeResponse(BaseResponse):
    _types = {
        "data": CreateWorkingHoursTypeResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateWorkingHoursTypeResponseBody] = None
        init(self, d, self._types)
