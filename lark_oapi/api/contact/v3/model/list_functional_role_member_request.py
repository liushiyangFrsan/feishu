# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListFunctionalRoleMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.role_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListFunctionalRoleMemberRequestBuilder":
        return ListFunctionalRoleMemberRequestBuilder()


class ListFunctionalRoleMemberRequestBuilder(object):

    def __init__(self,
                 list_functional_role_member_request: ListFunctionalRoleMemberRequest = ListFunctionalRoleMemberRequest()) -> None:
        list_functional_role_member_request.http_method = HttpMethod.GET
        list_functional_role_member_request.uri = "/open-apis/contact/v3/functional_roles/:role_id/members"
        list_functional_role_member_request.token_types = {AccessTokenType.TENANT}
        self._list_functional_role_member_request: ListFunctionalRoleMemberRequest = list_functional_role_member_request

    def page_size(self, page_size: int) -> "ListFunctionalRoleMemberRequestBuilder":
        self._list_functional_role_member_request.page_size = page_size
        self._list_functional_role_member_request.queries["page_size"] = str(page_size)
        return self

    def page_token(self, page_token: str) -> "ListFunctionalRoleMemberRequestBuilder":
        self._list_functional_role_member_request.page_token = page_token
        self._list_functional_role_member_request.queries["page_token"] = str(page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListFunctionalRoleMemberRequestBuilder":
        self._list_functional_role_member_request.user_id_type = user_id_type
        self._list_functional_role_member_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ListFunctionalRoleMemberRequestBuilder":
        self._list_functional_role_member_request.department_id_type = department_id_type
        self._list_functional_role_member_request.queries["department_id_type"] = str(department_id_type)
        return self

    def role_id(self, role_id: str) -> "ListFunctionalRoleMemberRequestBuilder":
        self._list_functional_role_member_request.role_id = role_id
        self._list_functional_role_member_request.paths["role_id"] = role_id
        return self

    def build(self) -> ListFunctionalRoleMemberRequest:
        return self._list_functional_role_member_request
