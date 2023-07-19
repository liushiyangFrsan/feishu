# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .table_merge_info import TableMergeInfo


class TableProperty(object):
    _types = {
        "row_size": int,
        "column_size": int,
        "column_width": List[int],
        "merge_info": List[TableMergeInfo],
    }

    def __init__(self, d):
        self.row_size: Optional[int] = None
        self.column_size: Optional[int] = None
        self.column_width: Optional[List[int]] = None
        self.merge_info: Optional[List[TableMergeInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TablePropertyBuilder":
        return TablePropertyBuilder()


class TablePropertyBuilder(object):
    def __init__(self, table_property: TableProperty = TableProperty({})) -> None:
        self._table_property: TableProperty = table_property

    def row_size(self, row_size: int) -> "TablePropertyBuilder":
        self._table_property.row_size = row_size
        return self

    def column_size(self, column_size: int) -> "TablePropertyBuilder":
        self._table_property.column_size = column_size
        return self

    def column_width(self, column_width: List[int]) -> "TablePropertyBuilder":
        self._table_property.column_width = column_width
        return self

    def merge_info(self, merge_info: List[TableMergeInfo]) -> "TablePropertyBuilder":
        self._table_property.merge_info = merge_info
        return self

    def build(self) -> "TableProperty":
        return self._table_property