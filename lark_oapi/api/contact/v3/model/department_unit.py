# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DepartmentUnit(object):
    _types = {
        "unit_id": str,
        "unit_type": str,
        "unit_name": str,
    }

    def __init__(self, d):
        self.unit_id: Optional[str] = None
        self.unit_type: Optional[str] = None
        self.unit_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentUnitBuilder":
        return DepartmentUnitBuilder()


class DepartmentUnitBuilder(object):
    def __init__(self, department_unit: DepartmentUnit = DepartmentUnit({})) -> None:
        self._department_unit: DepartmentUnit = department_unit

    def unit_id(self, unit_id: str) -> "DepartmentUnitBuilder":
        self._department_unit.unit_id = unit_id
        return self

    def unit_type(self, unit_type: str) -> "DepartmentUnitBuilder":
        self._department_unit.unit_type = unit_type
        return self

    def unit_name(self, unit_name: str) -> "DepartmentUnitBuilder":
        self._department_unit.unit_name = unit_name
        return self

    def build(self) -> "DepartmentUnit":
        return self._department_unit
