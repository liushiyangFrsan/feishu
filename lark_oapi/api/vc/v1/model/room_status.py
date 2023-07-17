# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RoomStatus(object):
    _types = {
        "status": bool,
        "schedule_status": bool,
        "disable_start_time": int,
        "disable_end_time": int,
        "disable_reason": str,
        "contact_ids": List[str],
        "disable_notice": bool,
        "resume_notice": bool,
    }

    def __init__(self, d):
        self.status: Optional[bool] = None
        self.schedule_status: Optional[bool] = None
        self.disable_start_time: Optional[int] = None
        self.disable_end_time: Optional[int] = None
        self.disable_reason: Optional[str] = None
        self.contact_ids: Optional[List[str]] = None
        self.disable_notice: Optional[bool] = None
        self.resume_notice: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoomStatusBuilder":
        return RoomStatusBuilder()


class RoomStatusBuilder(object):
    def __init__(self, room_status: RoomStatus = RoomStatus({})) -> None:
        self._room_status: RoomStatus = room_status

    def status(self, status: bool) -> "RoomStatusBuilder":
        self._room_status.status = status
        return self

    def schedule_status(self, schedule_status: bool) -> "RoomStatusBuilder":
        self._room_status.schedule_status = schedule_status
        return self

    def disable_start_time(self, disable_start_time: int) -> "RoomStatusBuilder":
        self._room_status.disable_start_time = disable_start_time
        return self

    def disable_end_time(self, disable_end_time: int) -> "RoomStatusBuilder":
        self._room_status.disable_end_time = disable_end_time
        return self

    def disable_reason(self, disable_reason: str) -> "RoomStatusBuilder":
        self._room_status.disable_reason = disable_reason
        return self

    def contact_ids(self, contact_ids: List[str]) -> "RoomStatusBuilder":
        self._room_status.contact_ids = contact_ids
        return self

    def disable_notice(self, disable_notice: bool) -> "RoomStatusBuilder":
        self._room_status.disable_notice = disable_notice
        return self

    def resume_notice(self, resume_notice: bool) -> "RoomStatusBuilder":
        self._room_status.resume_notice = resume_notice
        return self

    def build(self) -> "RoomStatus":
        return self._room_status
