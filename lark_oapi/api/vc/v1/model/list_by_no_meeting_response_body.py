# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .meeting import Meeting


class ListByNoMeetingResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "meeting_briefs": List[Meeting],
    }

    def __init__(self, d):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.meeting_briefs: Optional[List[Meeting]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListByNoMeetingResponseBodyBuilder":
        return ListByNoMeetingResponseBodyBuilder()


class ListByNoMeetingResponseBodyBuilder(object):
    def __init__(self, list_by_no_meeting_response_body: ListByNoMeetingResponseBody = ListByNoMeetingResponseBody(
        {})) -> None:
        self._list_by_no_meeting_response_body: ListByNoMeetingResponseBody = list_by_no_meeting_response_body

    def has_more(self, has_more: bool) -> "ListByNoMeetingResponseBodyBuilder":
        self._list_by_no_meeting_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListByNoMeetingResponseBodyBuilder":
        self._list_by_no_meeting_response_body.page_token = page_token
        return self

    def meeting_briefs(self, meeting_briefs: List[Meeting]) -> "ListByNoMeetingResponseBodyBuilder":
        self._list_by_no_meeting_response_body.meeting_briefs = meeting_briefs
        return self

    def build(self) -> "ListByNoMeetingResponseBody":
        return self._list_by_no_meeting_response_body
