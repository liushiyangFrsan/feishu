# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PstnSipInfo(object):
    _types = {
        "nickname": str,
        "main_address": str,
    }

    def __init__(self, d):
        self.nickname: Optional[str] = None
        self.main_address: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PstnSipInfoBuilder":
        return PstnSipInfoBuilder()


class PstnSipInfoBuilder(object):
    def __init__(self, pstn_sip_info: PstnSipInfo = PstnSipInfo({})) -> None:
        self._pstn_sip_info: PstnSipInfo = pstn_sip_info

    def nickname(self, nickname: str) -> "PstnSipInfoBuilder":
        self._pstn_sip_info.nickname = nickname
        return self

    def main_address(self, main_address: str) -> "PstnSipInfoBuilder":
        self._pstn_sip_info.main_address = main_address
        return self

    def build(self) -> "PstnSipInfo":
        return self._pstn_sip_info
