# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Vchat(object):
    _types = {
        "meeting_url": str,
        "vc_type": str,
    }

    def __init__(self, d):
        self.meeting_url: Optional[str] = None
        self.vc_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VchatBuilder":
        return VchatBuilder()


class VchatBuilder(object):
    def __init__(self, vchat: Vchat = Vchat({})) -> None:
        self._vchat: Vchat = vchat

    def meeting_url(self, meeting_url: str) -> "VchatBuilder":
        self._vchat.meeting_url = meeting_url
        return self

    def vc_type(self, vc_type: str) -> "VchatBuilder":
        self._vchat.vc_type = vc_type
        return self

    def build(self) -> "Vchat":
        return self._vchat
