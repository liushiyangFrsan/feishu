# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppI18nInfo(object):
    _types = {
        "i18n_key": str,
        "name": str,
        "description": str,
        "help_use": str,
    }

    def __init__(self, d):
        self.i18n_key: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.help_use: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppI18nInfoBuilder":
        return AppI18nInfoBuilder()


class AppI18nInfoBuilder(object):
    def __init__(self, app_i18n_info: AppI18nInfo = AppI18nInfo({})) -> None:
        self._app_i18n_info: AppI18nInfo = app_i18n_info

    def i18n_key(self, i18n_key: str) -> "AppI18nInfoBuilder":
        self._app_i18n_info.i18n_key = i18n_key
        return self

    def name(self, name: str) -> "AppI18nInfoBuilder":
        self._app_i18n_info.name = name
        return self

    def description(self, description: str) -> "AppI18nInfoBuilder":
        self._app_i18n_info.description = description
        return self

    def help_use(self, help_use: str) -> "AppI18nInfoBuilder":
        self._app_i18n_info.help_use = help_use
        return self

    def build(self) -> "AppI18nInfo":
        return self._app_i18n_info
