# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue


class TalentCombinedSnsInfo(object):
    _types = {
        "id": str,
        "sns_type": int,
        "link": str,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.sns_type: Optional[int] = None
        self.link: Optional[str] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCombinedSnsInfoBuilder":
        return TalentCombinedSnsInfoBuilder()


class TalentCombinedSnsInfoBuilder(object):
    def __init__(self, talent_combined_sns_info: TalentCombinedSnsInfo = TalentCombinedSnsInfo({})) -> None:
        self._talent_combined_sns_info: TalentCombinedSnsInfo = talent_combined_sns_info

    def id(self, id: str) -> "TalentCombinedSnsInfoBuilder":
        self._talent_combined_sns_info.id = id
        return self

    def sns_type(self, sns_type: int) -> "TalentCombinedSnsInfoBuilder":
        self._talent_combined_sns_info.sns_type = sns_type
        return self

    def link(self, link: str) -> "TalentCombinedSnsInfoBuilder":
        self._talent_combined_sns_info.link = link
        return self

    def customized_data(self, customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentCombinedSnsInfoBuilder":
        self._talent_combined_sns_info.customized_data = customized_data
        return self

    def build(self) -> "TalentCombinedSnsInfo":
        return self._talent_combined_sns_info
