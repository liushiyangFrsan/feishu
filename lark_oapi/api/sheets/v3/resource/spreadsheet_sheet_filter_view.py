# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.sheets.v3.model.create_spreadsheet_sheet_filter_view_request import \
    CreateSpreadsheetSheetFilterViewRequest
from lark_oapi.api.sheets.v3.model.create_spreadsheet_sheet_filter_view_response import \
    CreateSpreadsheetSheetFilterViewResponse
from lark_oapi.api.sheets.v3.model.delete_spreadsheet_sheet_filter_view_request import \
    DeleteSpreadsheetSheetFilterViewRequest
from lark_oapi.api.sheets.v3.model.delete_spreadsheet_sheet_filter_view_response import \
    DeleteSpreadsheetSheetFilterViewResponse
from lark_oapi.api.sheets.v3.model.get_spreadsheet_sheet_filter_view_request import GetSpreadsheetSheetFilterViewRequest
from lark_oapi.api.sheets.v3.model.get_spreadsheet_sheet_filter_view_response import \
    GetSpreadsheetSheetFilterViewResponse
from lark_oapi.api.sheets.v3.model.patch_spreadsheet_sheet_filter_view_request import \
    PatchSpreadsheetSheetFilterViewRequest
from lark_oapi.api.sheets.v3.model.patch_spreadsheet_sheet_filter_view_response import \
    PatchSpreadsheetSheetFilterViewResponse
from lark_oapi.api.sheets.v3.model.query_spreadsheet_sheet_filter_view_request import \
    QuerySpreadsheetSheetFilterViewRequest
from lark_oapi.api.sheets.v3.model.query_spreadsheet_sheet_filter_view_response import \
    QuerySpreadsheetSheetFilterViewResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class SpreadsheetSheetFilterView(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateSpreadsheetSheetFilterViewRequest,
               option: RequestOption = RequestOption()) -> CreateSpreadsheetSheetFilterViewResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateSpreadsheetSheetFilterViewResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            CreateSpreadsheetSheetFilterViewResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteSpreadsheetSheetFilterViewRequest,
               option: RequestOption = RequestOption()) -> DeleteSpreadsheetSheetFilterViewResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteSpreadsheetSheetFilterViewResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            DeleteSpreadsheetSheetFilterViewResponse)
        response.raw = resp

        return response

    def get(self, request: GetSpreadsheetSheetFilterViewRequest,
            option: RequestOption = RequestOption()) -> GetSpreadsheetSheetFilterViewResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetSpreadsheetSheetFilterViewResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                         GetSpreadsheetSheetFilterViewResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchSpreadsheetSheetFilterViewRequest,
              option: RequestOption = RequestOption()) -> PatchSpreadsheetSheetFilterViewResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchSpreadsheetSheetFilterViewResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           PatchSpreadsheetSheetFilterViewResponse)
        response.raw = resp

        return response

    def query(self, request: QuerySpreadsheetSheetFilterViewRequest,
              option: RequestOption = RequestOption()) -> QuerySpreadsheetSheetFilterViewResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QuerySpreadsheetSheetFilterViewResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           QuerySpreadsheetSheetFilterViewResponse)
        response.raw = resp

        return response
