# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_calendar_event_attendee_response_body import CreateCalendarEventAttendeeResponseBody


class CreateCalendarEventAttendeeResponse(BaseResponse):
    _types = {
        "data": CreateCalendarEventAttendeeResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateCalendarEventAttendeeResponseBody] = None
        init(self, d, self._types)
