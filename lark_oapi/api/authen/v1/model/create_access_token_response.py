# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_access_token_response_body import CreateAccessTokenResponseBody


class CreateAccessTokenResponse(BaseResponse):
    _types = {
        "data": CreateAccessTokenResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateAccessTokenResponseBody] = None
        init(self, d, self._types)
