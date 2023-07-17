# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .department_path_name import DepartmentPathName


class DepartmentPath(object):
    _types = {
        "department_ids": List[str],
        "department_path_name": DepartmentPathName,
    }

    def __init__(self, d):
        self.department_ids: Optional[List[str]] = None
        self.department_path_name: Optional[DepartmentPathName] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentPathBuilder":
        return DepartmentPathBuilder()


class DepartmentPathBuilder(object):
    def __init__(self, department_path: DepartmentPath = DepartmentPath({})) -> None:
        self._department_path: DepartmentPath = department_path

    def department_ids(self, department_ids: List[str]) -> "DepartmentPathBuilder":
        self._department_path.department_ids = department_ids
        return self

    def department_path_name(self, department_path_name: DepartmentPathName) -> "DepartmentPathBuilder":
        self._department_path.department_path_name = department_path_name
        return self

    def build(self) -> "DepartmentPath":
        return self._department_path
