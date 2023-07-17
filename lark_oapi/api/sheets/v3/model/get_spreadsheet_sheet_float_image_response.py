# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_spreadsheet_sheet_float_image_response_body import GetSpreadsheetSheetFloatImageResponseBody


class GetSpreadsheetSheetFloatImageResponse(BaseResponse):
    _types = {
        "data": GetSpreadsheetSheetFloatImageResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetSpreadsheetSheetFloatImageResponseBody] = None
        init(self, d, self._types)
