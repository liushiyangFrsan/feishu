# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .meeting import Meeting


class GetActiveMeetingReserveResponseBody(object):
    _types = {
        "meeting": Meeting,
    }

    def __init__(self, d):
        self.meeting: Optional[Meeting] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetActiveMeetingReserveResponseBodyBuilder":
        return GetActiveMeetingReserveResponseBodyBuilder()


class GetActiveMeetingReserveResponseBodyBuilder(object):
    def __init__(self,
                 get_active_meeting_reserve_response_body: GetActiveMeetingReserveResponseBody = GetActiveMeetingReserveResponseBody(
                     {})) -> None:
        self._get_active_meeting_reserve_response_body: GetActiveMeetingReserveResponseBody = get_active_meeting_reserve_response_body

    def meeting(self, meeting: Meeting) -> "GetActiveMeetingReserveResponseBodyBuilder":
        self._get_active_meeting_reserve_response_body.meeting = meeting
        return self

    def build(self) -> "GetActiveMeetingReserveResponseBody":
        return self._get_active_meeting_reserve_response_body
