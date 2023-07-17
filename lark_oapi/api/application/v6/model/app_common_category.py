# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppCommonCategory(object):
    _types = {
        "i18n_key": str,
        "category": str,
    }

    def __init__(self, d):
        self.i18n_key: Optional[str] = None
        self.category: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppCommonCategoryBuilder":
        return AppCommonCategoryBuilder()


class AppCommonCategoryBuilder(object):
    def __init__(self, app_common_category: AppCommonCategory = AppCommonCategory({})) -> None:
        self._app_common_category: AppCommonCategory = app_common_category

    def i18n_key(self, i18n_key: str) -> "AppCommonCategoryBuilder":
        self._app_common_category.i18n_key = i18n_key
        return self

    def category(self, category: str) -> "AppCommonCategoryBuilder":
        self._app_common_category.category = category
        return self

    def build(self) -> "AppCommonCategory":
        return self._app_common_category
