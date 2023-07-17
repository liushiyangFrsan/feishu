# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .interview import Interview


class ListApplicationInterviewResponseBody(object):
    _types = {
        "page_token": str,
        "has_more": bool,
        "items": List[Interview],
    }

    def __init__(self, d):
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.items: Optional[List[Interview]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListApplicationInterviewResponseBodyBuilder":
        return ListApplicationInterviewResponseBodyBuilder()


class ListApplicationInterviewResponseBodyBuilder(object):
    def __init__(self,
                 list_application_interview_response_body: ListApplicationInterviewResponseBody = ListApplicationInterviewResponseBody(
                     {})) -> None:
        self._list_application_interview_response_body: ListApplicationInterviewResponseBody = list_application_interview_response_body

    def page_token(self, page_token: str) -> "ListApplicationInterviewResponseBodyBuilder":
        self._list_application_interview_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListApplicationInterviewResponseBodyBuilder":
        self._list_application_interview_response_body.has_more = has_more
        return self

    def items(self, items: List[Interview]) -> "ListApplicationInterviewResponseBodyBuilder":
        self._list_application_interview_response_body.items = items
        return self

    def build(self) -> "ListApplicationInterviewResponseBody":
        return self._list_application_interview_response_body
