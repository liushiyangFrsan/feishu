# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_ticket_customized_field_response_body import GetTicketCustomizedFieldResponseBody


class GetTicketCustomizedFieldResponse(BaseResponse):
    _types = {
        "data": GetTicketCustomizedFieldResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetTicketCustomizedFieldResponseBody] = None
        init(self, d, self._types)
