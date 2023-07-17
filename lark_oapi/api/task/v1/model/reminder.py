# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Reminder(object):
    _types = {
        "id": int,
        "relative_fire_minute": int,
    }

    def __init__(self, d):
        self.id: Optional[int] = None
        self.relative_fire_minute: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReminderBuilder":
        return ReminderBuilder()


class ReminderBuilder(object):
    def __init__(self, reminder: Reminder = Reminder({})) -> None:
        self._reminder: Reminder = reminder

    def id(self, id: int) -> "ReminderBuilder":
        self._reminder.id = id
        return self

    def relative_fire_minute(self, relative_fire_minute: int) -> "ReminderBuilder":
        self._reminder.relative_fire_minute = relative_fire_minute
        return self

    def build(self) -> "Reminder":
        return self._reminder
