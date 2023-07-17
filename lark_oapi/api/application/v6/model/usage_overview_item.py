# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UsageOverviewItem(object):
    _types = {
        "page_view": int,
        "unique_visitor": int,
        "department_id": str,
    }

    def __init__(self, d):
        self.page_view: Optional[int] = None
        self.unique_visitor: Optional[int] = None
        self.department_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UsageOverviewItemBuilder":
        return UsageOverviewItemBuilder()


class UsageOverviewItemBuilder(object):
    def __init__(self, usage_overview_item: UsageOverviewItem = UsageOverviewItem({})) -> None:
        self._usage_overview_item: UsageOverviewItem = usage_overview_item

    def page_view(self, page_view: int) -> "UsageOverviewItemBuilder":
        self._usage_overview_item.page_view = page_view
        return self

    def unique_visitor(self, unique_visitor: int) -> "UsageOverviewItemBuilder":
        self._usage_overview_item.unique_visitor = unique_visitor
        return self

    def department_id(self, department_id: str) -> "UsageOverviewItemBuilder":
        self._usage_overview_item.department_id = department_id
        return self

    def build(self) -> "UsageOverviewItem":
        return self._usage_overview_item
