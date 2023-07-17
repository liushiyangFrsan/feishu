# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RemoveGroupMemberRequestBody(object):
    _types = {
        "member_type": str,
        "member_id": str,
        "member_id_type": str,
    }

    def __init__(self, d):
        self.member_type: Optional[str] = None
        self.member_id: Optional[str] = None
        self.member_id_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RemoveGroupMemberRequestBodyBuilder":
        return RemoveGroupMemberRequestBodyBuilder()


class RemoveGroupMemberRequestBodyBuilder(object):
    def __init__(self, remove_group_member_request_body: RemoveGroupMemberRequestBody = RemoveGroupMemberRequestBody(
        {})) -> None:
        self._remove_group_member_request_body: RemoveGroupMemberRequestBody = remove_group_member_request_body

    def member_type(self, member_type: str) -> "RemoveGroupMemberRequestBodyBuilder":
        self._remove_group_member_request_body.member_type = member_type
        return self

    def member_id(self, member_id: str) -> "RemoveGroupMemberRequestBodyBuilder":
        self._remove_group_member_request_body.member_id = member_id
        return self

    def member_id_type(self, member_id_type: str) -> "RemoveGroupMemberRequestBodyBuilder":
        self._remove_group_member_request_body.member_id_type = member_id_type
        return self

    def build(self) -> "RemoveGroupMemberRequestBody":
        return self._remove_group_member_request_body
