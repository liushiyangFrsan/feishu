# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetAppTableRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.text_field_as_array: Optional[bool] = None
        self.user_id_type: Optional[str] = None
        self.display_formula_ref: Optional[bool] = None
        self.automatic_fields: Optional[bool] = None
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.record_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetAppTableRecordRequestBuilder":
        return GetAppTableRecordRequestBuilder()


class GetAppTableRecordRequestBuilder(object):

    def __init__(self, get_app_table_record_request: GetAppTableRecordRequest = GetAppTableRecordRequest()) -> None:
        get_app_table_record_request.http_method = HttpMethod.GET
        get_app_table_record_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id"
        get_app_table_record_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_app_table_record_request: GetAppTableRecordRequest = get_app_table_record_request

    def text_field_as_array(self, text_field_as_array: bool) -> "GetAppTableRecordRequestBuilder":
        self._get_app_table_record_request.text_field_as_array = text_field_as_array
        self._get_app_table_record_request.queries["text_field_as_array"] = str(text_field_as_array)
        return self

    def user_id_type(self, user_id_type: str) -> "GetAppTableRecordRequestBuilder":
        self._get_app_table_record_request.user_id_type = user_id_type
        self._get_app_table_record_request.queries["user_id_type"] = str(user_id_type)
        return self

    def display_formula_ref(self, display_formula_ref: bool) -> "GetAppTableRecordRequestBuilder":
        self._get_app_table_record_request.display_formula_ref = display_formula_ref
        self._get_app_table_record_request.queries["display_formula_ref"] = str(display_formula_ref)
        return self

    def automatic_fields(self, automatic_fields: bool) -> "GetAppTableRecordRequestBuilder":
        self._get_app_table_record_request.automatic_fields = automatic_fields
        self._get_app_table_record_request.queries["automatic_fields"] = str(automatic_fields)
        return self

    def app_token(self, app_token: str) -> "GetAppTableRecordRequestBuilder":
        self._get_app_table_record_request.app_token = app_token
        self._get_app_table_record_request.paths["app_token"] = app_token
        return self

    def table_id(self, table_id: str) -> "GetAppTableRecordRequestBuilder":
        self._get_app_table_record_request.table_id = table_id
        self._get_app_table_record_request.paths["table_id"] = table_id
        return self

    def record_id(self, record_id: str) -> "GetAppTableRecordRequestBuilder":
        self._get_app_table_record_request.record_id = record_id
        self._get_app_table_record_request.paths["record_id"] = record_id
        return self

    def build(self) -> GetAppTableRecordRequest:
        return self._get_app_table_record_request
