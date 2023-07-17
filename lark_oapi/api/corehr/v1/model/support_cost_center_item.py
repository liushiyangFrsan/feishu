# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SupportCostCenterItem(object):
    _types = {
        "cost_center_id": str,
        "rate": int,
    }

    def __init__(self, d):
        self.cost_center_id: Optional[str] = None
        self.rate: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SupportCostCenterItemBuilder":
        return SupportCostCenterItemBuilder()


class SupportCostCenterItemBuilder(object):
    def __init__(self, support_cost_center_item: SupportCostCenterItem = SupportCostCenterItem({})) -> None:
        self._support_cost_center_item: SupportCostCenterItem = support_cost_center_item

    def cost_center_id(self, cost_center_id: str) -> "SupportCostCenterItemBuilder":
        self._support_cost_center_item.cost_center_id = cost_center_id
        return self

    def rate(self, rate: int) -> "SupportCostCenterItemBuilder":
        self._support_cost_center_item.rate = rate
        return self

    def build(self) -> "SupportCostCenterItem":
        return self._support_cost_center_item
