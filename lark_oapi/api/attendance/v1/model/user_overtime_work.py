# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserOvertimeWork(object):
    _types = {
        "approval_id": str,
        "duration": float,
        "unit": int,
        "category": int,
        "type": int,
        "start_time": str,
        "end_time": str,
    }

    def __init__(self, d):
        self.approval_id: Optional[str] = None
        self.duration: Optional[float] = None
        self.unit: Optional[int] = None
        self.category: Optional[int] = None
        self.type: Optional[int] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserOvertimeWorkBuilder":
        return UserOvertimeWorkBuilder()


class UserOvertimeWorkBuilder(object):
    def __init__(self, user_overtime_work: UserOvertimeWork = UserOvertimeWork({})) -> None:
        self._user_overtime_work: UserOvertimeWork = user_overtime_work

    def approval_id(self, approval_id: str) -> "UserOvertimeWorkBuilder":
        self._user_overtime_work.approval_id = approval_id
        return self

    def duration(self, duration: float) -> "UserOvertimeWorkBuilder":
        self._user_overtime_work.duration = duration
        return self

    def unit(self, unit: int) -> "UserOvertimeWorkBuilder":
        self._user_overtime_work.unit = unit
        return self

    def category(self, category: int) -> "UserOvertimeWorkBuilder":
        self._user_overtime_work.category = category
        return self

    def type(self, type: int) -> "UserOvertimeWorkBuilder":
        self._user_overtime_work.type = type
        return self

    def start_time(self, start_time: str) -> "UserOvertimeWorkBuilder":
        self._user_overtime_work.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "UserOvertimeWorkBuilder":
        self._user_overtime_work.end_time = end_time
        return self

    def build(self) -> "UserOvertimeWork":
        return self._user_overtime_work
