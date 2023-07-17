# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class AppAccessToken(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppAccessTokenBuilder":
        return AppAccessTokenBuilder()


class AppAccessTokenBuilder(object):
    def __init__(self, app_access_token: AppAccessToken = AppAccessToken({})) -> None:
        self._app_access_token: AppAccessToken = app_access_token

    def build(self) -> "AppAccessToken":
        return self._app_access_token
