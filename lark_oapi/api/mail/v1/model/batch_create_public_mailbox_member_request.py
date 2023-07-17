# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_create_public_mailbox_member_request_body import BatchCreatePublicMailboxMemberRequestBody


class BatchCreatePublicMailboxMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.public_mailbox_id: Optional[str] = None
        self.request_body: Optional[BatchCreatePublicMailboxMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchCreatePublicMailboxMemberRequestBuilder":
        return BatchCreatePublicMailboxMemberRequestBuilder()


class BatchCreatePublicMailboxMemberRequestBuilder(object):

    def __init__(self,
                 batch_create_public_mailbox_member_request: BatchCreatePublicMailboxMemberRequest = BatchCreatePublicMailboxMemberRequest()) -> None:
        batch_create_public_mailbox_member_request.http_method = HttpMethod.POST
        batch_create_public_mailbox_member_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/batch_create"
        batch_create_public_mailbox_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_create_public_mailbox_member_request: BatchCreatePublicMailboxMemberRequest = batch_create_public_mailbox_member_request

    def user_id_type(self, user_id_type: str) -> "BatchCreatePublicMailboxMemberRequestBuilder":
        self._batch_create_public_mailbox_member_request.user_id_type = user_id_type
        self._batch_create_public_mailbox_member_request.queries["user_id_type"] = str(user_id_type)
        return self

    def public_mailbox_id(self, public_mailbox_id: str) -> "BatchCreatePublicMailboxMemberRequestBuilder":
        self._batch_create_public_mailbox_member_request.public_mailbox_id = public_mailbox_id
        self._batch_create_public_mailbox_member_request.paths["public_mailbox_id"] = public_mailbox_id
        return self

    def request_body(self,
                     request_body: BatchCreatePublicMailboxMemberRequestBody) -> "BatchCreatePublicMailboxMemberRequestBuilder":
        self._batch_create_public_mailbox_member_request.request_body = request_body
        self._batch_create_public_mailbox_member_request.body = request_body
        return self

    def build(self) -> BatchCreatePublicMailboxMemberRequest:
        return self._batch_create_public_mailbox_member_request
