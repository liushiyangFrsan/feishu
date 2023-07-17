# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_id import UserId


class User(object):
    _types = {
        "id": UserId,
        "name": str,
    }

    def __init__(self, d):
        self.id: Optional[UserId] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserBuilder":
        return UserBuilder()


class UserBuilder(object):
    def __init__(self, user: User = User({})) -> None:
        self._user: User = user

    def id(self, id: UserId) -> "UserBuilder":
        self._user.id = id
        return self

    def name(self, name: str) -> "UserBuilder":
        self._user.name = name
        return self

    def build(self) -> "User":
        return self._user
