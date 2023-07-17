# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetMailgroupPermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.mailgroup_id: Optional[str] = None
        self.permission_member_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetMailgroupPermissionMemberRequestBuilder":
        return GetMailgroupPermissionMemberRequestBuilder()


class GetMailgroupPermissionMemberRequestBuilder(object):

    def __init__(self,
                 get_mailgroup_permission_member_request: GetMailgroupPermissionMemberRequest = GetMailgroupPermissionMemberRequest()) -> None:
        get_mailgroup_permission_member_request.http_method = HttpMethod.GET
        get_mailgroup_permission_member_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/permission_members/:permission_member_id"
        get_mailgroup_permission_member_request.token_types = {AccessTokenType.TENANT}
        self._get_mailgroup_permission_member_request: GetMailgroupPermissionMemberRequest = get_mailgroup_permission_member_request

    def user_id_type(self, user_id_type: str) -> "GetMailgroupPermissionMemberRequestBuilder":
        self._get_mailgroup_permission_member_request.user_id_type = user_id_type
        self._get_mailgroup_permission_member_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetMailgroupPermissionMemberRequestBuilder":
        self._get_mailgroup_permission_member_request.department_id_type = department_id_type
        self._get_mailgroup_permission_member_request.queries["department_id_type"] = str(department_id_type)
        return self

    def mailgroup_id(self, mailgroup_id: str) -> "GetMailgroupPermissionMemberRequestBuilder":
        self._get_mailgroup_permission_member_request.mailgroup_id = mailgroup_id
        self._get_mailgroup_permission_member_request.paths["mailgroup_id"] = mailgroup_id
        return self

    def permission_member_id(self, permission_member_id: str) -> "GetMailgroupPermissionMemberRequestBuilder":
        self._get_mailgroup_permission_member_request.permission_member_id = permission_member_id
        self._get_mailgroup_permission_member_request.paths["permission_member_id"] = permission_member_id
        return self

    def build(self) -> GetMailgroupPermissionMemberRequest:
        return self._get_mailgroup_permission_member_request
