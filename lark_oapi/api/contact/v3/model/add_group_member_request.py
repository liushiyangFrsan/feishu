# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .add_group_member_request_body import AddGroupMemberRequestBody


class AddGroupMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.group_id: Optional[str] = None
        self.request_body: Optional[AddGroupMemberRequestBody] = None

    @staticmethod
    def builder() -> "AddGroupMemberRequestBuilder":
        return AddGroupMemberRequestBuilder()


class AddGroupMemberRequestBuilder(object):

    def __init__(self, add_group_member_request: AddGroupMemberRequest = AddGroupMemberRequest()) -> None:
        add_group_member_request.http_method = HttpMethod.POST
        add_group_member_request.uri = "/open-apis/contact/v3/group/:group_id/member/add"
        add_group_member_request.token_types = {AccessTokenType.TENANT}
        self._add_group_member_request: AddGroupMemberRequest = add_group_member_request

    def group_id(self, group_id: str) -> "AddGroupMemberRequestBuilder":
        self._add_group_member_request.group_id = group_id
        self._add_group_member_request.paths["group_id"] = group_id
        return self

    def request_body(self, request_body: AddGroupMemberRequestBody) -> "AddGroupMemberRequestBuilder":
        self._add_group_member_request.request_body = request_body
        self._add_group_member_request.body = request_body
        return self

    def build(self) -> AddGroupMemberRequest:
        return self._add_group_member_request
