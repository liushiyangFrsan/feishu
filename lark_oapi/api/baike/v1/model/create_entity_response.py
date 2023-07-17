# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_entity_response_body import CreateEntityResponseBody


class CreateEntityResponse(BaseResponse):
    _types = {
        "data": CreateEntityResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateEntityResponseBody] = None
        init(self, d, self._types)
