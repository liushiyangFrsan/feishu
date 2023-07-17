# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OuterInfo(object):
    _types = {
        "provider": str,
        "outer_id": str,
    }

    def __init__(self, d):
        self.provider: Optional[str] = None
        self.outer_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OuterInfoBuilder":
        return OuterInfoBuilder()


class OuterInfoBuilder(object):
    def __init__(self, outer_info: OuterInfo = OuterInfo({})) -> None:
        self._outer_info: OuterInfo = outer_info

    def provider(self, provider: str) -> "OuterInfoBuilder":
        self._outer_info.provider = provider
        return self

    def outer_id(self, outer_id: str) -> "OuterInfoBuilder":
        self._outer_info.outer_id = outer_id
        return self

    def build(self) -> "OuterInfo":
        return self._outer_info
