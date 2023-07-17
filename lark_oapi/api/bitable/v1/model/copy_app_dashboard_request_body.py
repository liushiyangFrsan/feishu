# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CopyAppDashboardRequestBody(object):
    _types = {
        "name": str,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CopyAppDashboardRequestBodyBuilder":
        return CopyAppDashboardRequestBodyBuilder()


class CopyAppDashboardRequestBodyBuilder(object):
    def __init__(self, copy_app_dashboard_request_body: CopyAppDashboardRequestBody = CopyAppDashboardRequestBody(
        {})) -> None:
        self._copy_app_dashboard_request_body: CopyAppDashboardRequestBody = copy_app_dashboard_request_body

    def name(self, name: str) -> "CopyAppDashboardRequestBodyBuilder":
        self._copy_app_dashboard_request_body.name = name
        return self

    def build(self) -> "CopyAppDashboardRequestBody":
        return self._copy_app_dashboard_request_body
