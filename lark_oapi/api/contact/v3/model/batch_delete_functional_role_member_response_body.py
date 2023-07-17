# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .functional_role_member_result import FunctionalRoleMemberResult


class BatchDeleteFunctionalRoleMemberResponseBody(object):
    _types = {
        "result": List[FunctionalRoleMemberResult],
    }

    def __init__(self, d):
        self.result: Optional[List[FunctionalRoleMemberResult]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteFunctionalRoleMemberResponseBodyBuilder":
        return BatchDeleteFunctionalRoleMemberResponseBodyBuilder()


class BatchDeleteFunctionalRoleMemberResponseBodyBuilder(object):
    def __init__(self,
                 batch_delete_functional_role_member_response_body: BatchDeleteFunctionalRoleMemberResponseBody = BatchDeleteFunctionalRoleMemberResponseBody(
                     {})) -> None:
        self._batch_delete_functional_role_member_response_body: BatchDeleteFunctionalRoleMemberResponseBody = batch_delete_functional_role_member_response_body

    def result(self, result: List[FunctionalRoleMemberResult]) -> "BatchDeleteFunctionalRoleMemberResponseBodyBuilder":
        self._batch_delete_functional_role_member_response_body.result = result
        return self

    def build(self) -> "BatchDeleteFunctionalRoleMemberResponseBody":
        return self._batch_delete_functional_role_member_response_body
