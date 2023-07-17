# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppTableViewPropertyFilterInfoCondition(object):
    _types = {
        "field_id": str,
        "operator": str,
        "value": str,
        "condition_id": str,
        "field_type": str,
    }

    def __init__(self, d):
        self.field_id: Optional[str] = None
        self.operator: Optional[str] = None
        self.value: Optional[str] = None
        self.condition_id: Optional[str] = None
        self.field_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableViewPropertyFilterInfoConditionBuilder":
        return AppTableViewPropertyFilterInfoConditionBuilder()


class AppTableViewPropertyFilterInfoConditionBuilder(object):
    def __init__(self,
                 app_table_view_property_filter_info_condition: AppTableViewPropertyFilterInfoCondition = AppTableViewPropertyFilterInfoCondition(
                     {})) -> None:
        self._app_table_view_property_filter_info_condition: AppTableViewPropertyFilterInfoCondition = app_table_view_property_filter_info_condition

    def field_id(self, field_id: str) -> "AppTableViewPropertyFilterInfoConditionBuilder":
        self._app_table_view_property_filter_info_condition.field_id = field_id
        return self

    def operator(self, operator: str) -> "AppTableViewPropertyFilterInfoConditionBuilder":
        self._app_table_view_property_filter_info_condition.operator = operator
        return self

    def value(self, value: str) -> "AppTableViewPropertyFilterInfoConditionBuilder":
        self._app_table_view_property_filter_info_condition.value = value
        return self

    def condition_id(self, condition_id: str) -> "AppTableViewPropertyFilterInfoConditionBuilder":
        self._app_table_view_property_filter_info_condition.condition_id = condition_id
        return self

    def field_type(self, field_type: str) -> "AppTableViewPropertyFilterInfoConditionBuilder":
        self._app_table_view_property_filter_info_condition.field_type = field_type
        return self

    def build(self) -> "AppTableViewPropertyFilterInfoCondition":
        return self._app_table_view_property_filter_info_condition
