# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .leave_granting_record import LeaveGrantingRecord


class CreateLeaveGrantingRecordResponseBody(object):
    _types = {
        "leave_granting_record": LeaveGrantingRecord,
    }

    def __init__(self, d):
        self.leave_granting_record: Optional[LeaveGrantingRecord] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateLeaveGrantingRecordResponseBodyBuilder":
        return CreateLeaveGrantingRecordResponseBodyBuilder()


class CreateLeaveGrantingRecordResponseBodyBuilder(object):
    def __init__(self,
                 create_leave_granting_record_response_body: CreateLeaveGrantingRecordResponseBody = CreateLeaveGrantingRecordResponseBody(
                     {})) -> None:
        self._create_leave_granting_record_response_body: CreateLeaveGrantingRecordResponseBody = create_leave_granting_record_response_body

    def leave_granting_record(self,
                              leave_granting_record: LeaveGrantingRecord) -> "CreateLeaveGrantingRecordResponseBodyBuilder":
        self._create_leave_granting_record_response_body.leave_granting_record = leave_granting_record
        return self

    def build(self) -> "CreateLeaveGrantingRecordResponseBody":
        return self._create_leave_granting_record_response_body
