# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EvaluationTask(object):
    _types = {
        "id": str,
        "job_id": str,
        "talent_id": str,
        "application_id": str,
        "activity_status": int,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.activity_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EvaluationTaskBuilder":
        return EvaluationTaskBuilder()


class EvaluationTaskBuilder(object):
    def __init__(self, evaluation_task: EvaluationTask = EvaluationTask({})) -> None:
        self._evaluation_task: EvaluationTask = evaluation_task

    def id(self, id: str) -> "EvaluationTaskBuilder":
        self._evaluation_task.id = id
        return self

    def job_id(self, job_id: str) -> "EvaluationTaskBuilder":
        self._evaluation_task.job_id = job_id
        return self

    def talent_id(self, talent_id: str) -> "EvaluationTaskBuilder":
        self._evaluation_task.talent_id = talent_id
        return self

    def application_id(self, application_id: str) -> "EvaluationTaskBuilder":
        self._evaluation_task.application_id = application_id
        return self

    def activity_status(self, activity_status: int) -> "EvaluationTaskBuilder":
        self._evaluation_task.activity_status = activity_status
        return self

    def build(self) -> "EvaluationTask":
        return self._evaluation_task
