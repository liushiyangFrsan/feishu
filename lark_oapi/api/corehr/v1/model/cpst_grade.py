# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .cpst_currency import CpstCurrency
from .cpst_grade_standard_value import CpstGradeStandardValue
from .cpst_i18n import CpstI18n


class CpstGrade(object):
    _types = {
        "grade_id": str,
        "grade_tid": str,
        "grade_standard_value": CpstGradeStandardValue,
        "currency": CpstCurrency,
        "description": CpstI18n,
    }

    def __init__(self, d):
        self.grade_id: Optional[str] = None
        self.grade_tid: Optional[str] = None
        self.grade_standard_value: Optional[CpstGradeStandardValue] = None
        self.currency: Optional[CpstCurrency] = None
        self.description: Optional[CpstI18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CpstGradeBuilder":
        return CpstGradeBuilder()


class CpstGradeBuilder(object):
    def __init__(self, cpst_grade: CpstGrade = CpstGrade({})) -> None:
        self._cpst_grade: CpstGrade = cpst_grade

    def grade_id(self, grade_id: str) -> "CpstGradeBuilder":
        self._cpst_grade.grade_id = grade_id
        return self

    def grade_tid(self, grade_tid: str) -> "CpstGradeBuilder":
        self._cpst_grade.grade_tid = grade_tid
        return self

    def grade_standard_value(self, grade_standard_value: CpstGradeStandardValue) -> "CpstGradeBuilder":
        self._cpst_grade.grade_standard_value = grade_standard_value
        return self

    def currency(self, currency: CpstCurrency) -> "CpstGradeBuilder":
        self._cpst_grade.currency = currency
        return self

    def description(self, description: CpstI18n) -> "CpstGradeBuilder":
        self._cpst_grade.description = description
        return self

    def build(self) -> "CpstGrade":
        return self._cpst_grade
