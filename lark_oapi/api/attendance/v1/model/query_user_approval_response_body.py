# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_approval import UserApproval


class QueryUserApprovalResponseBody(object):
    _types = {
        "user_approvals": List[UserApproval],
    }

    def __init__(self, d):
        self.user_approvals: Optional[List[UserApproval]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserApprovalResponseBodyBuilder":
        return QueryUserApprovalResponseBodyBuilder()


class QueryUserApprovalResponseBodyBuilder(object):
    def __init__(self, query_user_approval_response_body: QueryUserApprovalResponseBody = QueryUserApprovalResponseBody(
        {})) -> None:
        self._query_user_approval_response_body: QueryUserApprovalResponseBody = query_user_approval_response_body

    def user_approvals(self, user_approvals: List[UserApproval]) -> "QueryUserApprovalResponseBodyBuilder":
        self._query_user_approval_response_body.user_approvals = user_approvals
        return self

    def build(self) -> "QueryUserApprovalResponseBody":
        return self._query_user_approval_response_body
