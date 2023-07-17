# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .room import Room


class MgetRoomResponseBody(object):
    _types = {
        "items": List[Room],
    }

    def __init__(self, d):
        self.items: Optional[List[Room]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MgetRoomResponseBodyBuilder":
        return MgetRoomResponseBodyBuilder()


class MgetRoomResponseBodyBuilder(object):
    def __init__(self, mget_room_response_body: MgetRoomResponseBody = MgetRoomResponseBody({})) -> None:
        self._mget_room_response_body: MgetRoomResponseBody = mget_room_response_body

    def items(self, items: List[Room]) -> "MgetRoomResponseBodyBuilder":
        self._mget_room_response_body.items = items
        return self

    def build(self) -> "MgetRoomResponseBody":
        return self._mget_room_response_body
