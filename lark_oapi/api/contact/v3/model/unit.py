# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Unit(object):
    _types = {
        "unit_id": str,
        "name": str,
        "unit_type": str,
    }

    def __init__(self, d):
        self.unit_id: Optional[str] = None
        self.name: Optional[str] = None
        self.unit_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UnitBuilder":
        return UnitBuilder()


class UnitBuilder(object):
    def __init__(self, unit: Unit = Unit({})) -> None:
        self._unit: Unit = unit

    def unit_id(self, unit_id: str) -> "UnitBuilder":
        self._unit.unit_id = unit_id
        return self

    def name(self, name: str) -> "UnitBuilder":
        self._unit.name = name
        return self

    def unit_type(self, unit_type: str) -> "UnitBuilder":
        self._unit.unit_type = unit_type
        return self

    def build(self) -> "Unit":
        return self._unit
