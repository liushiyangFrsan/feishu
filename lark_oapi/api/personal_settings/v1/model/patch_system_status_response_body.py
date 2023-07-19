# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .system_status import SystemStatus


class PatchSystemStatusResponseBody(object):
    _types = {
        "system_status": SystemStatus,
    }

    def __init__(self, d):
        self.system_status: Optional[SystemStatus] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchSystemStatusResponseBodyBuilder":
        return PatchSystemStatusResponseBodyBuilder()


class PatchSystemStatusResponseBodyBuilder(object):
    def __init__(self, patch_system_status_response_body: PatchSystemStatusResponseBody = PatchSystemStatusResponseBody(
        {})) -> None:
        self._patch_system_status_response_body: PatchSystemStatusResponseBody = patch_system_status_response_body

    def system_status(self, system_status: SystemStatus) -> "PatchSystemStatusResponseBodyBuilder":
        self._patch_system_status_response_body.system_status = system_status
        return self

    def build(self) -> "PatchSystemStatusResponseBody":
        return self._patch_system_status_response_body