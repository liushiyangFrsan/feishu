# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .enum import Enum
from .i18n import I18n
from .object_field_data import ObjectFieldData


class HiberarchyCommon(object):
    _types = {
        "parent_id": str,
        "name": List[I18n],
        "type": Enum,
        "active": bool,
        "effective_time": str,
        "expiration_time": str,
        "code": str,
        "description": List[I18n],
        "tree_order": str,
        "list_order": str,
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d):
        self.parent_id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.type: Optional[Enum] = None
        self.active: Optional[bool] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.code: Optional[str] = None
        self.description: Optional[List[I18n]] = None
        self.tree_order: Optional[str] = None
        self.list_order: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "HiberarchyCommonBuilder":
        return HiberarchyCommonBuilder()


class HiberarchyCommonBuilder(object):
    def __init__(self, hiberarchy_common: HiberarchyCommon = HiberarchyCommon({})) -> None:
        self._hiberarchy_common: HiberarchyCommon = hiberarchy_common

    def parent_id(self, parent_id: str) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.parent_id = parent_id
        return self

    def name(self, name: List[I18n]) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.name = name
        return self

    def type(self, type: Enum) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.type = type
        return self

    def active(self, active: bool) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.active = active
        return self

    def effective_time(self, effective_time: str) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.expiration_time = expiration_time
        return self

    def code(self, code: str) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.code = code
        return self

    def description(self, description: List[I18n]) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.description = description
        return self

    def tree_order(self, tree_order: str) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.tree_order = tree_order
        return self

    def list_order(self, list_order: str) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.list_order = list_order
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "HiberarchyCommonBuilder":
        self._hiberarchy_common.custom_fields = custom_fields
        return self

    def build(self) -> "HiberarchyCommon":
        return self._hiberarchy_common