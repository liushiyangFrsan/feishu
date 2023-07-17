# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_add_group_member_request_body import BatchAddGroupMemberRequestBody


class BatchAddGroupMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.group_id: Optional[str] = None
        self.request_body: Optional[BatchAddGroupMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchAddGroupMemberRequestBuilder":
        return BatchAddGroupMemberRequestBuilder()


class BatchAddGroupMemberRequestBuilder(object):

    def __init__(self,
                 batch_add_group_member_request: BatchAddGroupMemberRequest = BatchAddGroupMemberRequest()) -> None:
        batch_add_group_member_request.http_method = HttpMethod.POST
        batch_add_group_member_request.uri = "/open-apis/contact/v3/group/:group_id/member/batch_add"
        batch_add_group_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_add_group_member_request: BatchAddGroupMemberRequest = batch_add_group_member_request

    def group_id(self, group_id: str) -> "BatchAddGroupMemberRequestBuilder":
        self._batch_add_group_member_request.group_id = group_id
        self._batch_add_group_member_request.paths["group_id"] = group_id
        return self

    def request_body(self, request_body: BatchAddGroupMemberRequestBody) -> "BatchAddGroupMemberRequestBuilder":
        self._batch_add_group_member_request.request_body = request_body
        self._batch_add_group_member_request.body = request_body
        return self

    def build(self) -> BatchAddGroupMemberRequest:
        return self._batch_add_group_member_request
