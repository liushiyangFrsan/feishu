# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .task import Task


class PatchTaskResponseBody(object):
    _types = {
        "task": Task,
    }

    def __init__(self, d):
        self.task: Optional[Task] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchTaskResponseBodyBuilder":
        return PatchTaskResponseBodyBuilder()


class PatchTaskResponseBodyBuilder(object):
    def __init__(self, patch_task_response_body: PatchTaskResponseBody = PatchTaskResponseBody({})) -> None:
        self._patch_task_response_body: PatchTaskResponseBody = patch_task_response_body

    def task(self, task: Task) -> "PatchTaskResponseBodyBuilder":
        self._patch_task_response_body.task = task
        return self

    def build(self) -> "PatchTaskResponseBody":
        return self._patch_task_response_body
