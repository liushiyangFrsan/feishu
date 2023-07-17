# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .member_result import MemberResult


class BatchAddGroupMemberResponseBody(object):
    _types = {
        "results": List[MemberResult],
    }

    def __init__(self, d):
        self.results: Optional[List[MemberResult]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchAddGroupMemberResponseBodyBuilder":
        return BatchAddGroupMemberResponseBodyBuilder()


class BatchAddGroupMemberResponseBodyBuilder(object):
    def __init__(self,
                 batch_add_group_member_response_body: BatchAddGroupMemberResponseBody = BatchAddGroupMemberResponseBody(
                     {})) -> None:
        self._batch_add_group_member_response_body: BatchAddGroupMemberResponseBody = batch_add_group_member_response_body

    def results(self, results: List[MemberResult]) -> "BatchAddGroupMemberResponseBodyBuilder":
        self._batch_add_group_member_response_body.results = results
        return self

    def build(self) -> "BatchAddGroupMemberResponseBody":
        return self._batch_add_group_member_response_body
