# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_stats_data_feature import UserStatsDataFeature


class UserStatsDataCell(object):
    _types = {
        "code": str,
        "value": str,
        "features": List[UserStatsDataFeature],
        "title": str,
    }

    def __init__(self, d):
        self.code: Optional[str] = None
        self.value: Optional[str] = None
        self.features: Optional[List[UserStatsDataFeature]] = None
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserStatsDataCellBuilder":
        return UserStatsDataCellBuilder()


class UserStatsDataCellBuilder(object):
    def __init__(self, user_stats_data_cell: UserStatsDataCell = UserStatsDataCell({})) -> None:
        self._user_stats_data_cell: UserStatsDataCell = user_stats_data_cell

    def code(self, code: str) -> "UserStatsDataCellBuilder":
        self._user_stats_data_cell.code = code
        return self

    def value(self, value: str) -> "UserStatsDataCellBuilder":
        self._user_stats_data_cell.value = value
        return self

    def features(self, features: List[UserStatsDataFeature]) -> "UserStatsDataCellBuilder":
        self._user_stats_data_cell.features = features
        return self

    def title(self, title: str) -> "UserStatsDataCellBuilder":
        self._user_stats_data_cell.title = title
        return self

    def build(self) -> "UserStatsDataCell":
        return self._user_stats_data_cell
