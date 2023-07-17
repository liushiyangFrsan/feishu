# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppDashboard(object):
    _types = {
        "block_id": str,
        "name": str,
    }

    def __init__(self, d):
        self.block_id: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppDashboardBuilder":
        return AppDashboardBuilder()


class AppDashboardBuilder(object):
    def __init__(self, app_dashboard: AppDashboard = AppDashboard({})) -> None:
        self._app_dashboard: AppDashboard = app_dashboard

    def block_id(self, block_id: str) -> "AppDashboardBuilder":
        self._app_dashboard.block_id = block_id
        return self

    def name(self, name: str) -> "AppDashboardBuilder":
        self._app_dashboard.name = name
        return self

    def build(self) -> "AppDashboard":
        return self._app_dashboard
