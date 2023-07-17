# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .acl_scope_event import AclScopeEvent
from .user_id import UserId


class CalendarAclEvent(object):
    _types = {
        "acl_id": str,
        "role": str,
        "scope": AclScopeEvent,
        "user_id_list": List[UserId],
    }

    def __init__(self, d):
        self.acl_id: Optional[str] = None
        self.role: Optional[str] = None
        self.scope: Optional[AclScopeEvent] = None
        self.user_id_list: Optional[List[UserId]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CalendarAclEventBuilder":
        return CalendarAclEventBuilder()


class CalendarAclEventBuilder(object):
    def __init__(self, calendar_acl_event: CalendarAclEvent = CalendarAclEvent({})) -> None:
        self._calendar_acl_event: CalendarAclEvent = calendar_acl_event

    def acl_id(self, acl_id: str) -> "CalendarAclEventBuilder":
        self._calendar_acl_event.acl_id = acl_id
        return self

    def role(self, role: str) -> "CalendarAclEventBuilder":
        self._calendar_acl_event.role = role
        return self

    def scope(self, scope: AclScopeEvent) -> "CalendarAclEventBuilder":
        self._calendar_acl_event.scope = scope
        return self

    def user_id_list(self, user_id_list: List[UserId]) -> "CalendarAclEventBuilder":
        self._calendar_acl_event.user_id_list = user_id_list
        return self

    def build(self) -> "CalendarAclEvent":
        return self._calendar_acl_event
