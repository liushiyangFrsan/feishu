# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SearchRoomRequestBody(object):
    _types = {
        "custom_room_ids": List[str],
        "keyword": str,
        "room_level_id": str,
        "search_level_name": bool,
        "page_size": int,
        "page_token": str,
    }

    def __init__(self, d):
        self.custom_room_ids: Optional[List[str]] = None
        self.keyword: Optional[str] = None
        self.room_level_id: Optional[str] = None
        self.search_level_name: Optional[bool] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchRoomRequestBodyBuilder":
        return SearchRoomRequestBodyBuilder()


class SearchRoomRequestBodyBuilder(object):
    def __init__(self, search_room_request_body: SearchRoomRequestBody = SearchRoomRequestBody({})) -> None:
        self._search_room_request_body: SearchRoomRequestBody = search_room_request_body

    def custom_room_ids(self, custom_room_ids: List[str]) -> "SearchRoomRequestBodyBuilder":
        self._search_room_request_body.custom_room_ids = custom_room_ids
        return self

    def keyword(self, keyword: str) -> "SearchRoomRequestBodyBuilder":
        self._search_room_request_body.keyword = keyword
        return self

    def room_level_id(self, room_level_id: str) -> "SearchRoomRequestBodyBuilder":
        self._search_room_request_body.room_level_id = room_level_id
        return self

    def search_level_name(self, search_level_name: bool) -> "SearchRoomRequestBodyBuilder":
        self._search_room_request_body.search_level_name = search_level_name
        return self

    def page_size(self, page_size: int) -> "SearchRoomRequestBodyBuilder":
        self._search_room_request_body.page_size = page_size
        return self

    def page_token(self, page_token: str) -> "SearchRoomRequestBodyBuilder":
        self._search_room_request_body.page_token = page_token
        return self

    def build(self) -> "SearchRoomRequestBody":
        return self._search_room_request_body
