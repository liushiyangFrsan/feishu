# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .filter_view import FilterView


class PatchSpreadsheetSheetFilterViewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.filter_view_id: Optional[str] = None
        self.request_body: Optional[FilterView] = None

    @staticmethod
    def builder() -> "PatchSpreadsheetSheetFilterViewRequestBuilder":
        return PatchSpreadsheetSheetFilterViewRequestBuilder()


class PatchSpreadsheetSheetFilterViewRequestBuilder(object):

    def __init__(self,
                 patch_spreadsheet_sheet_filter_view_request: PatchSpreadsheetSheetFilterViewRequest = PatchSpreadsheetSheetFilterViewRequest()) -> None:
        patch_spreadsheet_sheet_filter_view_request.http_method = HttpMethod.PATCH
        patch_spreadsheet_sheet_filter_view_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id"
        patch_spreadsheet_sheet_filter_view_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_spreadsheet_sheet_filter_view_request: PatchSpreadsheetSheetFilterViewRequest = patch_spreadsheet_sheet_filter_view_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "PatchSpreadsheetSheetFilterViewRequestBuilder":
        self._patch_spreadsheet_sheet_filter_view_request.spreadsheet_token = spreadsheet_token
        self._patch_spreadsheet_sheet_filter_view_request.paths["spreadsheet_token"] = spreadsheet_token
        return self

    def sheet_id(self, sheet_id: str) -> "PatchSpreadsheetSheetFilterViewRequestBuilder":
        self._patch_spreadsheet_sheet_filter_view_request.sheet_id = sheet_id
        self._patch_spreadsheet_sheet_filter_view_request.paths["sheet_id"] = sheet_id
        return self

    def filter_view_id(self, filter_view_id: str) -> "PatchSpreadsheetSheetFilterViewRequestBuilder":
        self._patch_spreadsheet_sheet_filter_view_request.filter_view_id = filter_view_id
        self._patch_spreadsheet_sheet_filter_view_request.paths["filter_view_id"] = filter_view_id
        return self

    def request_body(self, request_body: FilterView) -> "PatchSpreadsheetSheetFilterViewRequestBuilder":
        self._patch_spreadsheet_sheet_filter_view_request.request_body = request_body
        self._patch_spreadsheet_sheet_filter_view_request.body = request_body
        return self

    def build(self) -> PatchSpreadsheetSheetFilterViewRequest:
        return self._patch_spreadsheet_sheet_filter_view_request
