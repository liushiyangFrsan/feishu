# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ObjectiveProgress(object):
    _types = {
        "zh": str,
        "en": str,
    }

    def __init__(self, d):
        self.zh: Optional[str] = None
        self.en: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ObjectiveProgressBuilder":
        return ObjectiveProgressBuilder()


class ObjectiveProgressBuilder(object):
    def __init__(self, objective_progress: ObjectiveProgress = ObjectiveProgress({})) -> None:
        self._objective_progress: ObjectiveProgress = objective_progress

    def zh(self, zh: str) -> "ObjectiveProgressBuilder":
        self._objective_progress.zh = zh
        return self

    def en(self, en: str) -> "ObjectiveProgressBuilder":
        self._objective_progress.en = en
        return self

    def build(self) -> "ObjectiveProgress":
        return self._objective_progress
