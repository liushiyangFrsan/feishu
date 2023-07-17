# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job import Job


class ListJobResponseBody(object):
    _types = {
        "items": List[Job],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[Job]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListJobResponseBodyBuilder":
        return ListJobResponseBodyBuilder()


class ListJobResponseBodyBuilder(object):
    def __init__(self, list_job_response_body: ListJobResponseBody = ListJobResponseBody({})) -> None:
        self._list_job_response_body: ListJobResponseBody = list_job_response_body

    def items(self, items: List[Job]) -> "ListJobResponseBodyBuilder":
        self._list_job_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListJobResponseBodyBuilder":
        self._list_job_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListJobResponseBodyBuilder":
        self._list_job_response_body.page_token = page_token
        return self

    def build(self) -> "ListJobResponseBody":
        return self._list_job_response_body
