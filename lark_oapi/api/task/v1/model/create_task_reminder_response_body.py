# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .reminder import Reminder


class CreateTaskReminderResponseBody(object):
    _types = {
        "reminder": Reminder,
    }

    def __init__(self, d):
        self.reminder: Optional[Reminder] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateTaskReminderResponseBodyBuilder":
        return CreateTaskReminderResponseBodyBuilder()


class CreateTaskReminderResponseBodyBuilder(object):
    def __init__(self,
                 create_task_reminder_response_body: CreateTaskReminderResponseBody = CreateTaskReminderResponseBody(
                     {})) -> None:
        self._create_task_reminder_response_body: CreateTaskReminderResponseBody = create_task_reminder_response_body

    def reminder(self, reminder: Reminder) -> "CreateTaskReminderResponseBodyBuilder":
        self._create_task_reminder_response_body.reminder = reminder
        return self

    def build(self) -> "CreateTaskReminderResponseBody":
        return self._create_task_reminder_response_body
