# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user import User


class UpdateUserResponseBody(object):
    _types = {
        "user": User,
    }

    def __init__(self, d):
        self.user: Optional[User] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateUserResponseBodyBuilder":
        return UpdateUserResponseBodyBuilder()


class UpdateUserResponseBodyBuilder(object):
    def __init__(self, update_user_response_body: UpdateUserResponseBody = UpdateUserResponseBody({})) -> None:
        self._update_user_response_body: UpdateUserResponseBody = update_user_response_body

    def user(self, user: User) -> "UpdateUserResponseBodyBuilder":
        self._update_user_response_body.user = user
        return self

    def build(self) -> "UpdateUserResponseBody":
        return self._update_user_response_body
