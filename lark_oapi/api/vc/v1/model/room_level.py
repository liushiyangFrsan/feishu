# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RoomLevel(object):
    _types = {
        "room_level_id": str,
        "name": str,
        "parent_id": str,
        "path": List[str],
        "has_child": bool,
        "custom_group_id": str,
    }

    def __init__(self, d):
        self.room_level_id: Optional[str] = None
        self.name: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.path: Optional[List[str]] = None
        self.has_child: Optional[bool] = None
        self.custom_group_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoomLevelBuilder":
        return RoomLevelBuilder()


class RoomLevelBuilder(object):
    def __init__(self, room_level: RoomLevel = RoomLevel({})) -> None:
        self._room_level: RoomLevel = room_level

    def room_level_id(self, room_level_id: str) -> "RoomLevelBuilder":
        self._room_level.room_level_id = room_level_id
        return self

    def name(self, name: str) -> "RoomLevelBuilder":
        self._room_level.name = name
        return self

    def parent_id(self, parent_id: str) -> "RoomLevelBuilder":
        self._room_level.parent_id = parent_id
        return self

    def path(self, path: List[str]) -> "RoomLevelBuilder":
        self._room_level.path = path
        return self

    def has_child(self, has_child: bool) -> "RoomLevelBuilder":
        self._room_level.has_child = has_child
        return self

    def custom_group_id(self, custom_group_id: str) -> "RoomLevelBuilder":
        self._room_level.custom_group_id = custom_group_id
        return self

    def build(self) -> "RoomLevel":
        return self._room_level
