# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.sheets.v3.model.create_spreadsheet_sheet_filter_request import CreateSpreadsheetSheetFilterRequest
from lark_oapi.api.sheets.v3.model.create_spreadsheet_sheet_filter_response import CreateSpreadsheetSheetFilterResponse
from lark_oapi.api.sheets.v3.model.delete_spreadsheet_sheet_filter_request import DeleteSpreadsheetSheetFilterRequest
from lark_oapi.api.sheets.v3.model.delete_spreadsheet_sheet_filter_response import DeleteSpreadsheetSheetFilterResponse
from lark_oapi.api.sheets.v3.model.get_spreadsheet_sheet_filter_request import GetSpreadsheetSheetFilterRequest
from lark_oapi.api.sheets.v3.model.get_spreadsheet_sheet_filter_response import GetSpreadsheetSheetFilterResponse
from lark_oapi.api.sheets.v3.model.update_spreadsheet_sheet_filter_request import UpdateSpreadsheetSheetFilterRequest
from lark_oapi.api.sheets.v3.model.update_spreadsheet_sheet_filter_response import UpdateSpreadsheetSheetFilterResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class SpreadsheetSheetFilter(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateSpreadsheetSheetFilterRequest,
               option: RequestOption = RequestOption()) -> CreateSpreadsheetSheetFilterResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateSpreadsheetSheetFilterResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        CreateSpreadsheetSheetFilterResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteSpreadsheetSheetFilterRequest,
               option: RequestOption = RequestOption()) -> DeleteSpreadsheetSheetFilterResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteSpreadsheetSheetFilterResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        DeleteSpreadsheetSheetFilterResponse)
        response.raw = resp

        return response

    def get(self, request: GetSpreadsheetSheetFilterRequest,
            option: RequestOption = RequestOption()) -> GetSpreadsheetSheetFilterResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetSpreadsheetSheetFilterResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     GetSpreadsheetSheetFilterResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateSpreadsheetSheetFilterRequest,
               option: RequestOption = RequestOption()) -> UpdateSpreadsheetSheetFilterResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateSpreadsheetSheetFilterResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        UpdateSpreadsheetSheetFilterResponse)
        response.raw = resp

        return response
