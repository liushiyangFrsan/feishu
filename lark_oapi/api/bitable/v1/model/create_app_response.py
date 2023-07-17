# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_app_response_body import CreateAppResponseBody


class CreateAppResponse(BaseResponse):
    _types = {
        "data": CreateAppResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateAppResponseBody] = None
        init(self, d, self._types)
