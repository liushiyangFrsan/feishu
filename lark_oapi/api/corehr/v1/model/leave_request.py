# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class LeaveRequest(object):
    _types = {
        "leave_request_id": str,
        "employment_id": str,
        "employment_name": List[I18n],
        "leave_type_id": str,
        "leave_type_name": List[I18n],
        "start_time": str,
        "end_time": str,
        "leave_duration": str,
        "leave_duration_unit": int,
        "leave_request_status": int,
        "grant_source": str,
        "return_time": str,
        "submitted_at": str,
        "submitted_by": str,
        "notes": str,
    }

    def __init__(self, d):
        self.leave_request_id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.employment_name: Optional[List[I18n]] = None
        self.leave_type_id: Optional[str] = None
        self.leave_type_name: Optional[List[I18n]] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.leave_duration: Optional[str] = None
        self.leave_duration_unit: Optional[int] = None
        self.leave_request_status: Optional[int] = None
        self.grant_source: Optional[str] = None
        self.return_time: Optional[str] = None
        self.submitted_at: Optional[str] = None
        self.submitted_by: Optional[str] = None
        self.notes: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveRequestBuilder":
        return LeaveRequestBuilder()


class LeaveRequestBuilder(object):
    def __init__(self, leave_request: LeaveRequest = LeaveRequest({})) -> None:
        self._leave_request: LeaveRequest = leave_request

    def leave_request_id(self, leave_request_id: str) -> "LeaveRequestBuilder":
        self._leave_request.leave_request_id = leave_request_id
        return self

    def employment_id(self, employment_id: str) -> "LeaveRequestBuilder":
        self._leave_request.employment_id = employment_id
        return self

    def employment_name(self, employment_name: List[I18n]) -> "LeaveRequestBuilder":
        self._leave_request.employment_name = employment_name
        return self

    def leave_type_id(self, leave_type_id: str) -> "LeaveRequestBuilder":
        self._leave_request.leave_type_id = leave_type_id
        return self

    def leave_type_name(self, leave_type_name: List[I18n]) -> "LeaveRequestBuilder":
        self._leave_request.leave_type_name = leave_type_name
        return self

    def start_time(self, start_time: str) -> "LeaveRequestBuilder":
        self._leave_request.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "LeaveRequestBuilder":
        self._leave_request.end_time = end_time
        return self

    def leave_duration(self, leave_duration: str) -> "LeaveRequestBuilder":
        self._leave_request.leave_duration = leave_duration
        return self

    def leave_duration_unit(self, leave_duration_unit: int) -> "LeaveRequestBuilder":
        self._leave_request.leave_duration_unit = leave_duration_unit
        return self

    def leave_request_status(self, leave_request_status: int) -> "LeaveRequestBuilder":
        self._leave_request.leave_request_status = leave_request_status
        return self

    def grant_source(self, grant_source: str) -> "LeaveRequestBuilder":
        self._leave_request.grant_source = grant_source
        return self

    def return_time(self, return_time: str) -> "LeaveRequestBuilder":
        self._leave_request.return_time = return_time
        return self

    def submitted_at(self, submitted_at: str) -> "LeaveRequestBuilder":
        self._leave_request.submitted_at = submitted_at
        return self

    def submitted_by(self, submitted_by: str) -> "LeaveRequestBuilder":
        self._leave_request.submitted_by = submitted_by
        return self

    def notes(self, notes: str) -> "LeaveRequestBuilder":
        self._leave_request.notes = notes
        return self

    def build(self) -> "LeaveRequest":
        return self._leave_request
