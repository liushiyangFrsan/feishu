# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateMailgroupMemberResponseBody(object):
    _types = {
        "member_id": str,
        "email": str,
        "user_id": str,
        "department_id": str,
        "type": str,
    }

    def __init__(self, d):
        self.member_id: Optional[str] = None
        self.email: Optional[str] = None
        self.user_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMailgroupMemberResponseBodyBuilder":
        return CreateMailgroupMemberResponseBodyBuilder()


class CreateMailgroupMemberResponseBodyBuilder(object):
    def __init__(self,
                 create_mailgroup_member_response_body: CreateMailgroupMemberResponseBody = CreateMailgroupMemberResponseBody(
                     {})) -> None:
        self._create_mailgroup_member_response_body: CreateMailgroupMemberResponseBody = create_mailgroup_member_response_body

    def member_id(self, member_id: str) -> "CreateMailgroupMemberResponseBodyBuilder":
        self._create_mailgroup_member_response_body.member_id = member_id
        return self

    def email(self, email: str) -> "CreateMailgroupMemberResponseBodyBuilder":
        self._create_mailgroup_member_response_body.email = email
        return self

    def user_id(self, user_id: str) -> "CreateMailgroupMemberResponseBodyBuilder":
        self._create_mailgroup_member_response_body.user_id = user_id
        return self

    def department_id(self, department_id: str) -> "CreateMailgroupMemberResponseBodyBuilder":
        self._create_mailgroup_member_response_body.department_id = department_id
        return self

    def type(self, type: str) -> "CreateMailgroupMemberResponseBodyBuilder":
        self._create_mailgroup_member_response_body.type = type
        return self

    def build(self) -> "CreateMailgroupMemberResponseBody":
        return self._create_mailgroup_member_response_body
