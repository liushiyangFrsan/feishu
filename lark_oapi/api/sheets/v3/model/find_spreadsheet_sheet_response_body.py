# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .find_replace_result import FindReplaceResult


class FindSpreadsheetSheetResponseBody(object):
    _types = {
        "find_result": FindReplaceResult,
    }

    def __init__(self, d):
        self.find_result: Optional[FindReplaceResult] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FindSpreadsheetSheetResponseBodyBuilder":
        return FindSpreadsheetSheetResponseBodyBuilder()


class FindSpreadsheetSheetResponseBodyBuilder(object):
    def __init__(self,
                 find_spreadsheet_sheet_response_body: FindSpreadsheetSheetResponseBody = FindSpreadsheetSheetResponseBody(
                     {})) -> None:
        self._find_spreadsheet_sheet_response_body: FindSpreadsheetSheetResponseBody = find_spreadsheet_sheet_response_body

    def find_result(self, find_result: FindReplaceResult) -> "FindSpreadsheetSheetResponseBodyBuilder":
        self._find_spreadsheet_sheet_response_body.find_result = find_result
        return self

    def build(self) -> "FindSpreadsheetSheetResponseBody":
        return self._find_spreadsheet_sheet_response_body
