# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .copy_app_dashboard_request_body import CopyAppDashboardRequestBody


class CopyAppDashboardRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.block_id: Optional[str] = None
        self.request_body: Optional[CopyAppDashboardRequestBody] = None

    @staticmethod
    def builder() -> "CopyAppDashboardRequestBuilder":
        return CopyAppDashboardRequestBuilder()


class CopyAppDashboardRequestBuilder(object):

    def __init__(self, copy_app_dashboard_request: CopyAppDashboardRequest = CopyAppDashboardRequest()) -> None:
        copy_app_dashboard_request.http_method = HttpMethod.POST
        copy_app_dashboard_request.uri = "/open-apis/bitable/v1/apps/:app_token/dashboards/:block_id/copy"
        copy_app_dashboard_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._copy_app_dashboard_request: CopyAppDashboardRequest = copy_app_dashboard_request

    def app_token(self, app_token: str) -> "CopyAppDashboardRequestBuilder":
        self._copy_app_dashboard_request.app_token = app_token
        self._copy_app_dashboard_request.paths["app_token"] = app_token
        return self

    def block_id(self, block_id: str) -> "CopyAppDashboardRequestBuilder":
        self._copy_app_dashboard_request.block_id = block_id
        self._copy_app_dashboard_request.paths["block_id"] = block_id
        return self

    def request_body(self, request_body: CopyAppDashboardRequestBody) -> "CopyAppDashboardRequestBuilder":
        self._copy_app_dashboard_request.request_body = request_body
        self._copy_app_dashboard_request.body = request_body
        return self

    def build(self) -> CopyAppDashboardRequest:
        return self._copy_app_dashboard_request
