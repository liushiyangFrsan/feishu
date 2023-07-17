# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_progress_record_response_body import UpdateProgressRecordResponseBody


class UpdateProgressRecordResponse(BaseResponse):
    _types = {
        "data": UpdateProgressRecordResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UpdateProgressRecordResponseBody] = None
        init(self, d, self._types)
