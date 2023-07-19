# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_visibility_event import AppVisibilityEvent


class AppVersionRemarkEvent(object):
    _types = {
        "remark": str,
        "update_remark": str,
        "visibility": AppVisibilityEvent,
    }

    def __init__(self, d):
        self.remark: Optional[str] = None
        self.update_remark: Optional[str] = None
        self.visibility: Optional[AppVisibilityEvent] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppVersionRemarkEventBuilder":
        return AppVersionRemarkEventBuilder()


class AppVersionRemarkEventBuilder(object):
    def __init__(self, app_version_remark_event: AppVersionRemarkEvent = AppVersionRemarkEvent({})) -> None:
        self._app_version_remark_event: AppVersionRemarkEvent = app_version_remark_event

    def remark(self, remark: str) -> "AppVersionRemarkEventBuilder":
        self._app_version_remark_event.remark = remark
        return self

    def update_remark(self, update_remark: str) -> "AppVersionRemarkEventBuilder":
        self._app_version_remark_event.update_remark = update_remark
        return self

    def visibility(self, visibility: AppVisibilityEvent) -> "AppVersionRemarkEventBuilder":
        self._app_version_remark_event.visibility = visibility
        return self

    def build(self) -> "AppVersionRemarkEvent":
        return self._app_version_remark_event