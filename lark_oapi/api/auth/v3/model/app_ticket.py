# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class AppTicket(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTicketBuilder":
        return AppTicketBuilder()


class AppTicketBuilder(object):
    def __init__(self, app_ticket: AppTicket = AppTicket({})) -> None:
        self._app_ticket: AppTicket = app_ticket

    def build(self) -> "AppTicket":
        return self._app_ticket