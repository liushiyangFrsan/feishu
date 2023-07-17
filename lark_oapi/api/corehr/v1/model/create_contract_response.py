# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_contract_response_body import CreateContractResponseBody


class CreateContractResponse(BaseResponse):
    _types = {
        "data": CreateContractResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateContractResponseBody] = None
        init(self, d, self._types)
