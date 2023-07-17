# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .calendar import Calendar


class PatchCalendarResponseBody(object):
    _types = {
        "calendar": Calendar,
    }

    def __init__(self, d):
        self.calendar: Optional[Calendar] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchCalendarResponseBodyBuilder":
        return PatchCalendarResponseBodyBuilder()


class PatchCalendarResponseBodyBuilder(object):
    def __init__(self, patch_calendar_response_body: PatchCalendarResponseBody = PatchCalendarResponseBody({})) -> None:
        self._patch_calendar_response_body: PatchCalendarResponseBody = patch_calendar_response_body

    def calendar(self, calendar: Calendar) -> "PatchCalendarResponseBodyBuilder":
        self._patch_calendar_response_body.calendar = calendar
        return self

    def build(self) -> "PatchCalendarResponseBody":
        return self._patch_calendar_response_body
