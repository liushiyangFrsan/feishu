# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_identity_response_body import CreateIdentityResponseBody


class CreateIdentityResponse(BaseResponse):
    _types = {
        "data": CreateIdentityResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateIdentityResponseBody] = None
        init(self, d, self._types)
