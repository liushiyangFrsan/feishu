# Code generated by Lark OpenAPI.

from .v4.resource import *


class CalendarService(object):
    def __init__(self, config: Config) -> None:
        self.v4: V4 = V4(config)


class V4(object):
    def __init__(self, config: Config) -> None:
        self.calendar: Optional[Calendar] = Calendar(config)
        self.calendar_acl: Optional[CalendarAcl] = CalendarAcl(config)
        self.calendar_event: Optional[CalendarEvent] = CalendarEvent(config)
        self.calendar_event_attendee: Optional[CalendarEventAttendee] = CalendarEventAttendee(config)
        self.calendar_event_attendee_chat_member: Optional[
            CalendarEventAttendeeChatMember] = CalendarEventAttendeeChatMember(config)
        self.exchange_binding: Optional[ExchangeBinding] = ExchangeBinding(config)
        self.freebusy: Optional[Freebusy] = Freebusy(config)
        self.setting: Optional[Setting] = Setting(config)
        self.timeoff_event: Optional[TimeoffEvent] = TimeoffEvent(config)
