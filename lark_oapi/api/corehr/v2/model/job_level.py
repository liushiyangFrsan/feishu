# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .custom_field_data import CustomFieldData
from .i18n import I18n


class JobLevel(object):
    _types = {
        "job_level_id": str,
        "level_order": int,
        "code": str,
        "name": List[I18n],
        "description": List[I18n],
        "active": bool,
        "custom_fields": List[CustomFieldData],
    }

    def __init__(self, d):
        self.job_level_id: Optional[str] = None
        self.level_order: Optional[int] = None
        self.code: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.description: Optional[List[I18n]] = None
        self.active: Optional[bool] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobLevelBuilder":
        return JobLevelBuilder()


class JobLevelBuilder(object):
    def __init__(self, job_level: JobLevel = JobLevel({})) -> None:
        self._job_level: JobLevel = job_level

    def job_level_id(self, job_level_id: str) -> "JobLevelBuilder":
        self._job_level.job_level_id = job_level_id
        return self

    def level_order(self, level_order: int) -> "JobLevelBuilder":
        self._job_level.level_order = level_order
        return self

    def code(self, code: str) -> "JobLevelBuilder":
        self._job_level.code = code
        return self

    def name(self, name: List[I18n]) -> "JobLevelBuilder":
        self._job_level.name = name
        return self

    def description(self, description: List[I18n]) -> "JobLevelBuilder":
        self._job_level.description = description
        return self

    def active(self, active: bool) -> "JobLevelBuilder":
        self._job_level.active = active
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "JobLevelBuilder":
        self._job_level.custom_fields = custom_fields
        return self

    def build(self) -> "JobLevel":
        return self._job_level
