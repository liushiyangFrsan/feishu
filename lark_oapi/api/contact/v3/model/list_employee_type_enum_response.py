# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_employee_type_enum_response_body import ListEmployeeTypeEnumResponseBody


class ListEmployeeTypeEnumResponse(BaseResponse):
    _types = {
        "data": ListEmployeeTypeEnumResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListEmployeeTypeEnumResponseBody] = None
        init(self, d, self._types)
