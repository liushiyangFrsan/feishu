# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_delete_calendar_event_attendee_request_body import BatchDeleteCalendarEventAttendeeRequestBody


class BatchDeleteCalendarEventAttendeeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.calendar_id: Optional[str] = None
        self.event_id: Optional[str] = None
        self.request_body: Optional[BatchDeleteCalendarEventAttendeeRequestBody] = None

    @staticmethod
    def builder() -> "BatchDeleteCalendarEventAttendeeRequestBuilder":
        return BatchDeleteCalendarEventAttendeeRequestBuilder()


class BatchDeleteCalendarEventAttendeeRequestBuilder(object):

    def __init__(self,
                 batch_delete_calendar_event_attendee_request: BatchDeleteCalendarEventAttendeeRequest = BatchDeleteCalendarEventAttendeeRequest()) -> None:
        batch_delete_calendar_event_attendee_request.http_method = HttpMethod.POST
        batch_delete_calendar_event_attendee_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id/attendees/batch_delete"
        batch_delete_calendar_event_attendee_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._batch_delete_calendar_event_attendee_request: BatchDeleteCalendarEventAttendeeRequest = batch_delete_calendar_event_attendee_request

    def user_id_type(self, user_id_type: str) -> "BatchDeleteCalendarEventAttendeeRequestBuilder":
        self._batch_delete_calendar_event_attendee_request.user_id_type = user_id_type
        self._batch_delete_calendar_event_attendee_request.queries["user_id_type"] = str(user_id_type)
        return self

    def calendar_id(self, calendar_id: str) -> "BatchDeleteCalendarEventAttendeeRequestBuilder":
        self._batch_delete_calendar_event_attendee_request.calendar_id = calendar_id
        self._batch_delete_calendar_event_attendee_request.paths["calendar_id"] = calendar_id
        return self

    def event_id(self, event_id: str) -> "BatchDeleteCalendarEventAttendeeRequestBuilder":
        self._batch_delete_calendar_event_attendee_request.event_id = event_id
        self._batch_delete_calendar_event_attendee_request.paths["event_id"] = event_id
        return self

    def request_body(self,
                     request_body: BatchDeleteCalendarEventAttendeeRequestBody) -> "BatchDeleteCalendarEventAttendeeRequestBuilder":
        self._batch_delete_calendar_event_attendee_request.request_body = request_body
        self._batch_delete_calendar_event_attendee_request.body = request_body
        return self

    def build(self) -> BatchDeleteCalendarEventAttendeeRequest:
        return self._batch_delete_calendar_event_attendee_request
