# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .object_field_data import ObjectFieldData


class JobFamily(object):
    _types = {
        "id": str,
        "name": List[I18n],
        "active": bool,
        "parent_id": str,
        "effective_time": str,
        "expiration_time": str,
        "code": str,
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.active: Optional[bool] = None
        self.parent_id: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.code: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobFamilyBuilder":
        return JobFamilyBuilder()


class JobFamilyBuilder(object):
    def __init__(self, job_family: JobFamily = JobFamily({})) -> None:
        self._job_family: JobFamily = job_family

    def id(self, id: str) -> "JobFamilyBuilder":
        self._job_family.id = id
        return self

    def name(self, name: List[I18n]) -> "JobFamilyBuilder":
        self._job_family.name = name
        return self

    def active(self, active: bool) -> "JobFamilyBuilder":
        self._job_family.active = active
        return self

    def parent_id(self, parent_id: str) -> "JobFamilyBuilder":
        self._job_family.parent_id = parent_id
        return self

    def effective_time(self, effective_time: str) -> "JobFamilyBuilder":
        self._job_family.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "JobFamilyBuilder":
        self._job_family.expiration_time = expiration_time
        return self

    def code(self, code: str) -> "JobFamilyBuilder":
        self._job_family.code = code
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "JobFamilyBuilder":
        self._job_family.custom_fields = custom_fields
        return self

    def build(self) -> "JobFamily":
        return self._job_family
