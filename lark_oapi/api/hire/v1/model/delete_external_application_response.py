# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .delete_external_application_response_body import DeleteExternalApplicationResponseBody


class DeleteExternalApplicationResponse(BaseResponse):
    _types = {
        "data": DeleteExternalApplicationResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[DeleteExternalApplicationResponseBody] = None
        init(self, d, self._types)