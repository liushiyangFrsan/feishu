# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .upload_file_response_body import UploadFileResponseBody


class UploadFileResponse(BaseResponse):
    _types = {
        "data": UploadFileResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UploadFileResponseBody] = None
        init(self, d, self._types)
