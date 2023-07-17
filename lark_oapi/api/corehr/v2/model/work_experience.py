# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WorkExperience(object):
    _types = {
        "company_name": str,
        "start_time": str,
        "end_time": str,
        "job_title": str,
        "description": str,
    }

    def __init__(self, d):
        self.company_name: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.job_title: Optional[str] = None
        self.description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkExperienceBuilder":
        return WorkExperienceBuilder()


class WorkExperienceBuilder(object):
    def __init__(self, work_experience: WorkExperience = WorkExperience({})) -> None:
        self._work_experience: WorkExperience = work_experience

    def company_name(self, company_name: str) -> "WorkExperienceBuilder":
        self._work_experience.company_name = company_name
        return self

    def start_time(self, start_time: str) -> "WorkExperienceBuilder":
        self._work_experience.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "WorkExperienceBuilder":
        self._work_experience.end_time = end_time
        return self

    def job_title(self, job_title: str) -> "WorkExperienceBuilder":
        self._work_experience.job_title = job_title
        return self

    def description(self, description: str) -> "WorkExperienceBuilder":
        self._work_experience.description = description
        return self

    def build(self) -> "WorkExperience":
        return self._work_experience
