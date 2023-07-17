# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SubscribeUser(object):
    _types = {
        "user_id": int,
        "user_name": str,
    }

    def __init__(self, d):
        self.user_id: Optional[int] = None
        self.user_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubscribeUserBuilder":
        return SubscribeUserBuilder()


class SubscribeUserBuilder(object):
    def __init__(self, subscribe_user: SubscribeUser = SubscribeUser({})) -> None:
        self._subscribe_user: SubscribeUser = subscribe_user

    def user_id(self, user_id: int) -> "SubscribeUserBuilder":
        self._subscribe_user.user_id = user_id
        return self

    def user_name(self, user_name: str) -> "SubscribeUserBuilder":
        self._subscribe_user.user_name = user_name
        return self

    def build(self) -> "SubscribeUser":
        return self._subscribe_user
