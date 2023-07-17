# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .department import Department


class ChildrenDepartmentResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[Department],
    }

    def __init__(self, d):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[Department]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChildrenDepartmentResponseBodyBuilder":
        return ChildrenDepartmentResponseBodyBuilder()


class ChildrenDepartmentResponseBodyBuilder(object):
    def __init__(self,
                 children_department_response_body: ChildrenDepartmentResponseBody = ChildrenDepartmentResponseBody(
                     {})) -> None:
        self._children_department_response_body: ChildrenDepartmentResponseBody = children_department_response_body

    def has_more(self, has_more: bool) -> "ChildrenDepartmentResponseBodyBuilder":
        self._children_department_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ChildrenDepartmentResponseBodyBuilder":
        self._children_department_response_body.page_token = page_token
        return self

    def items(self, items: List[Department]) -> "ChildrenDepartmentResponseBodyBuilder":
        self._children_department_response_body.items = items
        return self

    def build(self) -> "ChildrenDepartmentResponseBody":
        return self._children_department_response_body
