# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_category_response_body import CreateCategoryResponseBody


class CreateCategoryResponse(BaseResponse):
    _types = {
        "data": CreateCategoryResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateCategoryResponseBody] = None
        init(self, d, self._types)
