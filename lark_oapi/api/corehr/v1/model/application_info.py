# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApplicationInfo(object):
    _types = {
        "apply_initiator_id": str,
        "apply_initiating_time": str,
        "apply_finish_time": str,
        "process_id": str,
    }

    def __init__(self, d):
        self.apply_initiator_id: Optional[str] = None
        self.apply_initiating_time: Optional[str] = None
        self.apply_finish_time: Optional[str] = None
        self.process_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationInfoBuilder":
        return ApplicationInfoBuilder()


class ApplicationInfoBuilder(object):
    def __init__(self, application_info: ApplicationInfo = ApplicationInfo({})) -> None:
        self._application_info: ApplicationInfo = application_info

    def apply_initiator_id(self, apply_initiator_id: str) -> "ApplicationInfoBuilder":
        self._application_info.apply_initiator_id = apply_initiator_id
        return self

    def apply_initiating_time(self, apply_initiating_time: str) -> "ApplicationInfoBuilder":
        self._application_info.apply_initiating_time = apply_initiating_time
        return self

    def apply_finish_time(self, apply_finish_time: str) -> "ApplicationInfoBuilder":
        self._application_info.apply_finish_time = apply_finish_time
        return self

    def process_id(self, process_id: str) -> "ApplicationInfoBuilder":
        self._application_info.process_id = process_id
        return self

    def build(self) -> "ApplicationInfo":
        return self._application_info
