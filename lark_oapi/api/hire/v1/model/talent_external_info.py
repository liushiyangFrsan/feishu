# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TalentExternalInfo(object):
    _types = {
        "talent_id": str,
        "external_create_time": str,
    }

    def __init__(self, d):
        self.talent_id: Optional[str] = None
        self.external_create_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentExternalInfoBuilder":
        return TalentExternalInfoBuilder()


class TalentExternalInfoBuilder(object):
    def __init__(self, talent_external_info: TalentExternalInfo = TalentExternalInfo({})) -> None:
        self._talent_external_info: TalentExternalInfo = talent_external_info

    def talent_id(self, talent_id: str) -> "TalentExternalInfoBuilder":
        self._talent_external_info.talent_id = talent_id
        return self

    def external_create_time(self, external_create_time: str) -> "TalentExternalInfoBuilder":
        self._talent_external_info.external_create_time = external_create_time
        return self

    def build(self) -> "TalentExternalInfo":
        return self._talent_external_info
