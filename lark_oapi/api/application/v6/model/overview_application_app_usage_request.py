# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .overview_application_app_usage_request_body import OverviewApplicationAppUsageRequestBody


class OverviewApplicationAppUsageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.app_id: Optional[str] = None
        self.request_body: Optional[OverviewApplicationAppUsageRequestBody] = None

    @staticmethod
    def builder() -> "OverviewApplicationAppUsageRequestBuilder":
        return OverviewApplicationAppUsageRequestBuilder()


class OverviewApplicationAppUsageRequestBuilder(object):

    def __init__(self,
                 overview_application_app_usage_request: OverviewApplicationAppUsageRequest = OverviewApplicationAppUsageRequest()) -> None:
        overview_application_app_usage_request.http_method = HttpMethod.POST
        overview_application_app_usage_request.uri = "/open-apis/application/v6/applications/:app_id/app_usage/overview"
        overview_application_app_usage_request.token_types = {AccessTokenType.TENANT}
        self._overview_application_app_usage_request: OverviewApplicationAppUsageRequest = overview_application_app_usage_request

    def department_id_type(self, department_id_type: str) -> "OverviewApplicationAppUsageRequestBuilder":
        self._overview_application_app_usage_request.department_id_type = department_id_type
        self._overview_application_app_usage_request.queries["department_id_type"] = str(department_id_type)
        return self

    def app_id(self, app_id: str) -> "OverviewApplicationAppUsageRequestBuilder":
        self._overview_application_app_usage_request.app_id = app_id
        self._overview_application_app_usage_request.paths["app_id"] = app_id
        return self

    def request_body(self,
                     request_body: OverviewApplicationAppUsageRequestBody) -> "OverviewApplicationAppUsageRequestBuilder":
        self._overview_application_app_usage_request.request_body = request_body
        self._overview_application_app_usage_request.body = request_body
        return self

    def build(self) -> OverviewApplicationAppUsageRequest:
        return self._overview_application_app_usage_request
