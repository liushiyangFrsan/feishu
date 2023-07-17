# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ListFreebusyRequestBody(object):
    _types = {
        "time_min": str,
        "time_max": str,
        "user_id": str,
        "room_id": str,
    }

    def __init__(self, d):
        self.time_min: Optional[str] = None
        self.time_max: Optional[str] = None
        self.user_id: Optional[str] = None
        self.room_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListFreebusyRequestBodyBuilder":
        return ListFreebusyRequestBodyBuilder()


class ListFreebusyRequestBodyBuilder(object):
    def __init__(self, list_freebusy_request_body: ListFreebusyRequestBody = ListFreebusyRequestBody({})) -> None:
        self._list_freebusy_request_body: ListFreebusyRequestBody = list_freebusy_request_body

    def time_min(self, time_min: str) -> "ListFreebusyRequestBodyBuilder":
        self._list_freebusy_request_body.time_min = time_min
        return self

    def time_max(self, time_max: str) -> "ListFreebusyRequestBodyBuilder":
        self._list_freebusy_request_body.time_max = time_max
        return self

    def user_id(self, user_id: str) -> "ListFreebusyRequestBodyBuilder":
        self._list_freebusy_request_body.user_id = user_id
        return self

    def room_id(self, room_id: str) -> "ListFreebusyRequestBodyBuilder":
        self._list_freebusy_request_body.room_id = room_id
        return self

    def build(self) -> "ListFreebusyRequestBody":
        return self._list_freebusy_request_body
