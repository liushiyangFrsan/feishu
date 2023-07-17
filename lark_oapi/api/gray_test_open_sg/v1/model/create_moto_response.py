# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_moto_response_body import CreateMotoResponseBody


class CreateMotoResponse(BaseResponse):
    _types = {
        "data": CreateMotoResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateMotoResponseBody] = None
        init(self, d, self._types)
