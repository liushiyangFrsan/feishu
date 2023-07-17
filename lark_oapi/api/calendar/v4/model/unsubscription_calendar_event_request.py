# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class UnsubscriptionCalendarEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.calendar_id: Optional[str] = None

    @staticmethod
    def builder() -> "UnsubscriptionCalendarEventRequestBuilder":
        return UnsubscriptionCalendarEventRequestBuilder()


class UnsubscriptionCalendarEventRequestBuilder(object):

    def __init__(self,
                 unsubscription_calendar_event_request: UnsubscriptionCalendarEventRequest = UnsubscriptionCalendarEventRequest()) -> None:
        unsubscription_calendar_event_request.http_method = HttpMethod.POST
        unsubscription_calendar_event_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/unsubscription"
        unsubscription_calendar_event_request.token_types = {AccessTokenType.USER}
        self._unsubscription_calendar_event_request: UnsubscriptionCalendarEventRequest = unsubscription_calendar_event_request

    def calendar_id(self, calendar_id: str) -> "UnsubscriptionCalendarEventRequestBuilder":
        self._unsubscription_calendar_event_request.calendar_id = calendar_id
        self._unsubscription_calendar_event_request.paths["calendar_id"] = calendar_id
        return self

    def build(self) -> UnsubscriptionCalendarEventRequest:
        return self._unsubscription_calendar_event_request
