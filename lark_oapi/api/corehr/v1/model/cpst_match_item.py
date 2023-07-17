# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .cpst_grade import CpstGrade


class CpstMatchItem(object):
    _types = {
        "standard_id": str,
        "grade": CpstGrade,
        "effective_time": str,
    }

    def __init__(self, d):
        self.standard_id: Optional[str] = None
        self.grade: Optional[CpstGrade] = None
        self.effective_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CpstMatchItemBuilder":
        return CpstMatchItemBuilder()


class CpstMatchItemBuilder(object):
    def __init__(self, cpst_match_item: CpstMatchItem = CpstMatchItem({})) -> None:
        self._cpst_match_item: CpstMatchItem = cpst_match_item

    def standard_id(self, standard_id: str) -> "CpstMatchItemBuilder":
        self._cpst_match_item.standard_id = standard_id
        return self

    def grade(self, grade: CpstGrade) -> "CpstMatchItemBuilder":
        self._cpst_match_item.grade = grade
        return self

    def effective_time(self, effective_time: str) -> "CpstMatchItemBuilder":
        self._cpst_match_item.effective_time = effective_time
        return self

    def build(self) -> "CpstMatchItem":
        return self._cpst_match_item
