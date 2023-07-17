# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_national_id_type_response_body import CreateNationalIdTypeResponseBody


class CreateNationalIdTypeResponse(BaseResponse):
    _types = {
        "data": CreateNationalIdTypeResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateNationalIdTypeResponseBody] = None
        init(self, d, self._types)
