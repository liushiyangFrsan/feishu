# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_working_hours_type_response_body import PatchWorkingHoursTypeResponseBody


class PatchWorkingHoursTypeResponse(BaseResponse):
    _types = {
        "data": PatchWorkingHoursTypeResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[PatchWorkingHoursTypeResponseBody] = None
        init(self, d, self._types)
