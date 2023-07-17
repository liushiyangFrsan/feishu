# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListAppRoleMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.app_token: Optional[str] = None
        self.role_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListAppRoleMemberRequestBuilder":
        return ListAppRoleMemberRequestBuilder()


class ListAppRoleMemberRequestBuilder(object):

    def __init__(self, list_app_role_member_request: ListAppRoleMemberRequest = ListAppRoleMemberRequest()) -> None:
        list_app_role_member_request.http_method = HttpMethod.GET
        list_app_role_member_request.uri = "/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members"
        list_app_role_member_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_app_role_member_request: ListAppRoleMemberRequest = list_app_role_member_request

    def page_size(self, page_size: int) -> "ListAppRoleMemberRequestBuilder":
        self._list_app_role_member_request.page_size = page_size
        self._list_app_role_member_request.queries["page_size"] = str(page_size)
        return self

    def page_token(self, page_token: str) -> "ListAppRoleMemberRequestBuilder":
        self._list_app_role_member_request.page_token = page_token
        self._list_app_role_member_request.queries["page_token"] = str(page_token)
        return self

    def app_token(self, app_token: str) -> "ListAppRoleMemberRequestBuilder":
        self._list_app_role_member_request.app_token = app_token
        self._list_app_role_member_request.paths["app_token"] = app_token
        return self

    def role_id(self, role_id: str) -> "ListAppRoleMemberRequestBuilder":
        self._list_app_role_member_request.role_id = role_id
        self._list_app_role_member_request.paths["role_id"] = role_id
        return self

    def build(self) -> ListAppRoleMemberRequest:
        return self._list_app_role_member_request
