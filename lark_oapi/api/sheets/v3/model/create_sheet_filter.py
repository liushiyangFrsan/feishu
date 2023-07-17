# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .condition import Condition


class CreateSheetFilter(object):
    _types = {
        "range": str,
        "col": str,
        "condition": Condition,
    }

    def __init__(self, d):
        self.range: Optional[str] = None
        self.col: Optional[str] = None
        self.condition: Optional[Condition] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSheetFilterBuilder":
        return CreateSheetFilterBuilder()


class CreateSheetFilterBuilder(object):
    def __init__(self, create_sheet_filter: CreateSheetFilter = CreateSheetFilter({})) -> None:
        self._create_sheet_filter: CreateSheetFilter = create_sheet_filter

    def range(self, range: str) -> "CreateSheetFilterBuilder":
        self._create_sheet_filter.range = range
        return self

    def col(self, col: str) -> "CreateSheetFilterBuilder":
        self._create_sheet_filter.col = col
        return self

    def condition(self, condition: Condition) -> "CreateSheetFilterBuilder":
        self._create_sheet_filter.condition = condition
        return self

    def build(self) -> "CreateSheetFilter":
        return self._create_sheet_filter
