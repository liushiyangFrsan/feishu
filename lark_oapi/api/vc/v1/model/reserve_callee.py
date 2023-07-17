# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .pstn_sip_info import PstnSipInfo


class ReserveCallee(object):
    _types = {
        "id": str,
        "user_type": int,
        "pstn_sip_info": PstnSipInfo,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.user_type: Optional[int] = None
        self.pstn_sip_info: Optional[PstnSipInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveCalleeBuilder":
        return ReserveCalleeBuilder()


class ReserveCalleeBuilder(object):
    def __init__(self, reserve_callee: ReserveCallee = ReserveCallee({})) -> None:
        self._reserve_callee: ReserveCallee = reserve_callee

    def id(self, id: str) -> "ReserveCalleeBuilder":
        self._reserve_callee.id = id
        return self

    def user_type(self, user_type: int) -> "ReserveCalleeBuilder":
        self._reserve_callee.user_type = user_type
        return self

    def pstn_sip_info(self, pstn_sip_info: PstnSipInfo) -> "ReserveCalleeBuilder":
        self._reserve_callee.pstn_sip_info = pstn_sip_info
        return self

    def build(self) -> "ReserveCallee":
        return self._reserve_callee
