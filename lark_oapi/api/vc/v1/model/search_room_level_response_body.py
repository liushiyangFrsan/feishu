# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SearchRoomLevelResponseBody(object):
    _types = {
        "level_ids": List[str],
    }

    def __init__(self, d):
        self.level_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchRoomLevelResponseBodyBuilder":
        return SearchRoomLevelResponseBodyBuilder()


class SearchRoomLevelResponseBodyBuilder(object):
    def __init__(self, search_room_level_response_body: SearchRoomLevelResponseBody = SearchRoomLevelResponseBody(
        {})) -> None:
        self._search_room_level_response_body: SearchRoomLevelResponseBody = search_room_level_response_body

    def level_ids(self, level_ids: List[str]) -> "SearchRoomLevelResponseBodyBuilder":
        self._search_room_level_response_body.level_ids = level_ids
        return self

    def build(self) -> "SearchRoomLevelResponseBody":
        return self._search_room_level_response_body