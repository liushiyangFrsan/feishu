# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppScope(object):
    _types = {
        "scope": str,
        "description": str,
        "level": int,
    }

    def __init__(self, d):
        self.scope: Optional[str] = None
        self.description: Optional[str] = None
        self.level: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppScopeBuilder":
        return AppScopeBuilder()


class AppScopeBuilder(object):
    def __init__(self, app_scope: AppScope = AppScope({})) -> None:
        self._app_scope: AppScope = app_scope

    def scope(self, scope: str) -> "AppScopeBuilder":
        self._app_scope.scope = scope
        return self

    def description(self, description: str) -> "AppScopeBuilder":
        self._app_scope.description = description
        return self

    def level(self, level: int) -> "AppScopeBuilder":
        self._app_scope.level = level
        return self

    def build(self) -> "AppScope":
        return self._app_scope
