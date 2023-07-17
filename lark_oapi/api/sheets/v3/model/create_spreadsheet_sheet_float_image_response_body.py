# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .float_image import FloatImage


class CreateSpreadsheetSheetFloatImageResponseBody(object):
    _types = {
        "float_image": FloatImage,
    }

    def __init__(self, d):
        self.float_image: Optional[FloatImage] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSpreadsheetSheetFloatImageResponseBodyBuilder":
        return CreateSpreadsheetSheetFloatImageResponseBodyBuilder()


class CreateSpreadsheetSheetFloatImageResponseBodyBuilder(object):
    def __init__(self,
                 create_spreadsheet_sheet_float_image_response_body: CreateSpreadsheetSheetFloatImageResponseBody = CreateSpreadsheetSheetFloatImageResponseBody(
                     {})) -> None:
        self._create_spreadsheet_sheet_float_image_response_body: CreateSpreadsheetSheetFloatImageResponseBody = create_spreadsheet_sheet_float_image_response_body

    def float_image(self, float_image: FloatImage) -> "CreateSpreadsheetSheetFloatImageResponseBodyBuilder":
        self._create_spreadsheet_sheet_float_image_response_body.float_image = float_image
        return self

    def build(self) -> "CreateSpreadsheetSheetFloatImageResponseBody":
        return self._create_spreadsheet_sheet_float_image_response_body
