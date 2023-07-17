# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TaskApprove(object):
    _types = {
        "approval_code": str,
        "instance_code": str,
        "user_id": str,
        "comment": str,
        "task_id": str,
        "form": str,
    }

    def __init__(self, d):
        self.approval_code: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.user_id: Optional[str] = None
        self.comment: Optional[str] = None
        self.task_id: Optional[str] = None
        self.form: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskApproveBuilder":
        return TaskApproveBuilder()


class TaskApproveBuilder(object):
    def __init__(self, task_approve: TaskApprove = TaskApprove({})) -> None:
        self._task_approve: TaskApprove = task_approve

    def approval_code(self, approval_code: str) -> "TaskApproveBuilder":
        self._task_approve.approval_code = approval_code
        return self

    def instance_code(self, instance_code: str) -> "TaskApproveBuilder":
        self._task_approve.instance_code = instance_code
        return self

    def user_id(self, user_id: str) -> "TaskApproveBuilder":
        self._task_approve.user_id = user_id
        return self

    def comment(self, comment: str) -> "TaskApproveBuilder":
        self._task_approve.comment = comment
        return self

    def task_id(self, task_id: str) -> "TaskApproveBuilder":
        self._task_approve.task_id = task_id
        return self

    def form(self, form: str) -> "TaskApproveBuilder":
        self._task_approve.form = form
        return self

    def build(self) -> "TaskApprove":
        return self._task_approve
