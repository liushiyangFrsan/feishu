# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserRole(object):
    _types = {
        "user_id": str,
        "role_id": str,
        "modify_time": str,
    }

    def __init__(self, d):
        self.user_id: Optional[str] = None
        self.role_id: Optional[str] = None
        self.modify_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserRoleBuilder":
        return UserRoleBuilder()


class UserRoleBuilder(object):
    def __init__(self, user_role: UserRole = UserRole({})) -> None:
        self._user_role: UserRole = user_role

    def user_id(self, user_id: str) -> "UserRoleBuilder":
        self._user_role.user_id = user_id
        return self

    def role_id(self, role_id: str) -> "UserRoleBuilder":
        self._user_role.role_id = role_id
        return self

    def modify_time(self, modify_time: str) -> "UserRoleBuilder":
        self._user_role.modify_time = modify_time
        return self

    def build(self) -> "UserRole":
        return self._user_role
