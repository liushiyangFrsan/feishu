# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListMailgroupMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.mailgroup_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListMailgroupMemberRequestBuilder":
        return ListMailgroupMemberRequestBuilder()


class ListMailgroupMemberRequestBuilder(object):

    def __init__(self,
                 list_mailgroup_member_request: ListMailgroupMemberRequest = ListMailgroupMemberRequest()) -> None:
        list_mailgroup_member_request.http_method = HttpMethod.GET
        list_mailgroup_member_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/members"
        list_mailgroup_member_request.token_types = {AccessTokenType.TENANT}
        self._list_mailgroup_member_request: ListMailgroupMemberRequest = list_mailgroup_member_request

    def user_id_type(self, user_id_type: str) -> "ListMailgroupMemberRequestBuilder":
        self._list_mailgroup_member_request.user_id_type = user_id_type
        self._list_mailgroup_member_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ListMailgroupMemberRequestBuilder":
        self._list_mailgroup_member_request.department_id_type = department_id_type
        self._list_mailgroup_member_request.queries["department_id_type"] = str(department_id_type)
        return self

    def page_token(self, page_token: str) -> "ListMailgroupMemberRequestBuilder":
        self._list_mailgroup_member_request.page_token = page_token
        self._list_mailgroup_member_request.queries["page_token"] = str(page_token)
        return self

    def page_size(self, page_size: int) -> "ListMailgroupMemberRequestBuilder":
        self._list_mailgroup_member_request.page_size = page_size
        self._list_mailgroup_member_request.queries["page_size"] = str(page_size)
        return self

    def mailgroup_id(self, mailgroup_id: str) -> "ListMailgroupMemberRequestBuilder":
        self._list_mailgroup_member_request.mailgroup_id = mailgroup_id
        self._list_mailgroup_member_request.paths["mailgroup_id"] = mailgroup_id
        return self

    def build(self) -> ListMailgroupMemberRequest:
        return self._list_mailgroup_member_request
