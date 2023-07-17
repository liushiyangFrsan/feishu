# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateNotificationResponseBody(object):
    _types = {
        "notification_id": str,
        "status": int,
    }

    def __init__(self, d):
        self.notification_id: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateNotificationResponseBodyBuilder":
        return CreateNotificationResponseBodyBuilder()


class CreateNotificationResponseBodyBuilder(object):
    def __init__(self,
                 create_notification_response_body: CreateNotificationResponseBody = CreateNotificationResponseBody(
                     {})) -> None:
        self._create_notification_response_body: CreateNotificationResponseBody = create_notification_response_body

    def notification_id(self, notification_id: str) -> "CreateNotificationResponseBodyBuilder":
        self._create_notification_response_body.notification_id = notification_id
        return self

    def status(self, status: int) -> "CreateNotificationResponseBodyBuilder":
        self._create_notification_response_body.status = status
        return self

    def build(self) -> "CreateNotificationResponseBody":
        return self._create_notification_response_body
