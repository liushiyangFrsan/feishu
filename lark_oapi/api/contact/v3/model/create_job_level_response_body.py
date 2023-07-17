# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_level import JobLevel


class CreateJobLevelResponseBody(object):
    _types = {
        "job_level": JobLevel,
    }

    def __init__(self, d):
        self.job_level: Optional[JobLevel] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateJobLevelResponseBodyBuilder":
        return CreateJobLevelResponseBodyBuilder()


class CreateJobLevelResponseBodyBuilder(object):
    def __init__(self,
                 create_job_level_response_body: CreateJobLevelResponseBody = CreateJobLevelResponseBody({})) -> None:
        self._create_job_level_response_body: CreateJobLevelResponseBody = create_job_level_response_body

    def job_level(self, job_level: JobLevel) -> "CreateJobLevelResponseBodyBuilder":
        self._create_job_level_response_body.job_level = job_level
        return self

    def build(self) -> "CreateJobLevelResponseBody":
        return self._create_job_level_response_body
