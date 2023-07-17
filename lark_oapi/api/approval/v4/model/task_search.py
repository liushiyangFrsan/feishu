# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TaskSearch(object):
    _types = {
        "user_id": str,
        "approval_code": str,
        "instance_code": str,
        "instance_external_id": str,
        "group_external_id": str,
        "task_title": str,
        "task_status": str,
        "task_start_time_from": int,
        "task_start_time_to": int,
        "locale": str,
        "task_status_list": List[str],
        "order": int,
    }

    def __init__(self, d):
        self.user_id: Optional[str] = None
        self.approval_code: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.instance_external_id: Optional[str] = None
        self.group_external_id: Optional[str] = None
        self.task_title: Optional[str] = None
        self.task_status: Optional[str] = None
        self.task_start_time_from: Optional[int] = None
        self.task_start_time_to: Optional[int] = None
        self.locale: Optional[str] = None
        self.task_status_list: Optional[List[str]] = None
        self.order: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskSearchBuilder":
        return TaskSearchBuilder()


class TaskSearchBuilder(object):
    def __init__(self, task_search: TaskSearch = TaskSearch({})) -> None:
        self._task_search: TaskSearch = task_search

    def user_id(self, user_id: str) -> "TaskSearchBuilder":
        self._task_search.user_id = user_id
        return self

    def approval_code(self, approval_code: str) -> "TaskSearchBuilder":
        self._task_search.approval_code = approval_code
        return self

    def instance_code(self, instance_code: str) -> "TaskSearchBuilder":
        self._task_search.instance_code = instance_code
        return self

    def instance_external_id(self, instance_external_id: str) -> "TaskSearchBuilder":
        self._task_search.instance_external_id = instance_external_id
        return self

    def group_external_id(self, group_external_id: str) -> "TaskSearchBuilder":
        self._task_search.group_external_id = group_external_id
        return self

    def task_title(self, task_title: str) -> "TaskSearchBuilder":
        self._task_search.task_title = task_title
        return self

    def task_status(self, task_status: str) -> "TaskSearchBuilder":
        self._task_search.task_status = task_status
        return self

    def task_start_time_from(self, task_start_time_from: int) -> "TaskSearchBuilder":
        self._task_search.task_start_time_from = task_start_time_from
        return self

    def task_start_time_to(self, task_start_time_to: int) -> "TaskSearchBuilder":
        self._task_search.task_start_time_to = task_start_time_to
        return self

    def locale(self, locale: str) -> "TaskSearchBuilder":
        self._task_search.locale = locale
        return self

    def task_status_list(self, task_status_list: List[str]) -> "TaskSearchBuilder":
        self._task_search.task_status_list = task_status_list
        return self

    def order(self, order: int) -> "TaskSearchBuilder":
        self._task_search.order = order
        return self

    def build(self) -> "TaskSearch":
        return self._task_search
