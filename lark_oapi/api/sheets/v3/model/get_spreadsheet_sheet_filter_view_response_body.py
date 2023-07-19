# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .filter_view import FilterView


class GetSpreadsheetSheetFilterViewResponseBody(object):
    _types = {
        "filter_view": FilterView,
    }

    def __init__(self, d):
        self.filter_view: Optional[FilterView] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetSpreadsheetSheetFilterViewResponseBodyBuilder":
        return GetSpreadsheetSheetFilterViewResponseBodyBuilder()


class GetSpreadsheetSheetFilterViewResponseBodyBuilder(object):
    def __init__(self,
                 get_spreadsheet_sheet_filter_view_response_body: GetSpreadsheetSheetFilterViewResponseBody = GetSpreadsheetSheetFilterViewResponseBody(
                     {})) -> None:
        self._get_spreadsheet_sheet_filter_view_response_body: GetSpreadsheetSheetFilterViewResponseBody = get_spreadsheet_sheet_filter_view_response_body

    def filter_view(self, filter_view: FilterView) -> "GetSpreadsheetSheetFilterViewResponseBodyBuilder":
        self._get_spreadsheet_sheet_filter_view_response_body.filter_view = filter_view
        return self

    def build(self) -> "GetSpreadsheetSheetFilterViewResponseBody":
        return self._get_spreadsheet_sheet_filter_view_response_body