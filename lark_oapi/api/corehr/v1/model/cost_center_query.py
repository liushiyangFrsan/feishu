# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .object_field_data import ObjectFieldData
from .support_cost_center_item import SupportCostCenterItem


class CostCenterQuery(object):
    _types = {
        "is_autogenerate": bool,
        "id": str,
        "name": List[I18n],
        "active": bool,
        "code": str,
        "description": List[I18n],
        "effective_time": str,
        "expiration_time": str,
        "managers": List[str],
        "parent": str,
        "custom_fields": List[ObjectFieldData],
        "employment_id": str,
        "rate": int,
        "support_cost_center": List[SupportCostCenterItem],
    }

    def __init__(self, d):
        self.is_autogenerate: Optional[bool] = None
        self.id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.active: Optional[bool] = None
        self.code: Optional[str] = None
        self.description: Optional[List[I18n]] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.managers: Optional[List[str]] = None
        self.parent: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        self.employment_id: Optional[str] = None
        self.rate: Optional[int] = None
        self.support_cost_center: Optional[List[SupportCostCenterItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CostCenterQueryBuilder":
        return CostCenterQueryBuilder()


class CostCenterQueryBuilder(object):
    def __init__(self, cost_center_query: CostCenterQuery = CostCenterQuery({})) -> None:
        self._cost_center_query: CostCenterQuery = cost_center_query

    def is_autogenerate(self, is_autogenerate: bool) -> "CostCenterQueryBuilder":
        self._cost_center_query.is_autogenerate = is_autogenerate
        return self

    def id(self, id: str) -> "CostCenterQueryBuilder":
        self._cost_center_query.id = id
        return self

    def name(self, name: List[I18n]) -> "CostCenterQueryBuilder":
        self._cost_center_query.name = name
        return self

    def active(self, active: bool) -> "CostCenterQueryBuilder":
        self._cost_center_query.active = active
        return self

    def code(self, code: str) -> "CostCenterQueryBuilder":
        self._cost_center_query.code = code
        return self

    def description(self, description: List[I18n]) -> "CostCenterQueryBuilder":
        self._cost_center_query.description = description
        return self

    def effective_time(self, effective_time: str) -> "CostCenterQueryBuilder":
        self._cost_center_query.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "CostCenterQueryBuilder":
        self._cost_center_query.expiration_time = expiration_time
        return self

    def managers(self, managers: List[str]) -> "CostCenterQueryBuilder":
        self._cost_center_query.managers = managers
        return self

    def parent(self, parent: str) -> "CostCenterQueryBuilder":
        self._cost_center_query.parent = parent
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "CostCenterQueryBuilder":
        self._cost_center_query.custom_fields = custom_fields
        return self

    def employment_id(self, employment_id: str) -> "CostCenterQueryBuilder":
        self._cost_center_query.employment_id = employment_id
        return self

    def rate(self, rate: int) -> "CostCenterQueryBuilder":
        self._cost_center_query.rate = rate
        return self

    def support_cost_center(self, support_cost_center: List[SupportCostCenterItem]) -> "CostCenterQueryBuilder":
        self._cost_center_query.support_cost_center = support_cost_center
        return self

    def build(self) -> "CostCenterQuery":
        return self._cost_center_query
