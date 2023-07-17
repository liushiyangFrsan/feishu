# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_remove_group_member_request_body import BatchRemoveGroupMemberRequestBody


class BatchRemoveGroupMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.group_id: Optional[str] = None
        self.request_body: Optional[BatchRemoveGroupMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchRemoveGroupMemberRequestBuilder":
        return BatchRemoveGroupMemberRequestBuilder()


class BatchRemoveGroupMemberRequestBuilder(object):

    def __init__(self,
                 batch_remove_group_member_request: BatchRemoveGroupMemberRequest = BatchRemoveGroupMemberRequest()) -> None:
        batch_remove_group_member_request.http_method = HttpMethod.POST
        batch_remove_group_member_request.uri = "/open-apis/contact/v3/group/:group_id/member/batch_remove"
        batch_remove_group_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_remove_group_member_request: BatchRemoveGroupMemberRequest = batch_remove_group_member_request

    def group_id(self, group_id: str) -> "BatchRemoveGroupMemberRequestBuilder":
        self._batch_remove_group_member_request.group_id = group_id
        self._batch_remove_group_member_request.paths["group_id"] = group_id
        return self

    def request_body(self, request_body: BatchRemoveGroupMemberRequestBody) -> "BatchRemoveGroupMemberRequestBuilder":
        self._batch_remove_group_member_request.request_body = request_body
        self._batch_remove_group_member_request.body = request_body
        return self

    def build(self) -> BatchRemoveGroupMemberRequest:
        return self._batch_remove_group_member_request
