# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListPublicMailboxMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.public_mailbox_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListPublicMailboxMemberRequestBuilder":
        return ListPublicMailboxMemberRequestBuilder()


class ListPublicMailboxMemberRequestBuilder(object):

    def __init__(self,
                 list_public_mailbox_member_request: ListPublicMailboxMemberRequest = ListPublicMailboxMemberRequest()) -> None:
        list_public_mailbox_member_request.http_method = HttpMethod.GET
        list_public_mailbox_member_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members"
        list_public_mailbox_member_request.token_types = {AccessTokenType.TENANT}
        self._list_public_mailbox_member_request: ListPublicMailboxMemberRequest = list_public_mailbox_member_request

    def user_id_type(self, user_id_type: str) -> "ListPublicMailboxMemberRequestBuilder":
        self._list_public_mailbox_member_request.user_id_type = user_id_type
        self._list_public_mailbox_member_request.queries["user_id_type"] = str(user_id_type)
        return self

    def page_token(self, page_token: str) -> "ListPublicMailboxMemberRequestBuilder":
        self._list_public_mailbox_member_request.page_token = page_token
        self._list_public_mailbox_member_request.queries["page_token"] = str(page_token)
        return self

    def page_size(self, page_size: int) -> "ListPublicMailboxMemberRequestBuilder":
        self._list_public_mailbox_member_request.page_size = page_size
        self._list_public_mailbox_member_request.queries["page_size"] = str(page_size)
        return self

    def public_mailbox_id(self, public_mailbox_id: str) -> "ListPublicMailboxMemberRequestBuilder":
        self._list_public_mailbox_member_request.public_mailbox_id = public_mailbox_id
        self._list_public_mailbox_member_request.paths["public_mailbox_id"] = public_mailbox_id
        return self

    def build(self) -> ListPublicMailboxMemberRequest:
        return self._list_public_mailbox_member_request
