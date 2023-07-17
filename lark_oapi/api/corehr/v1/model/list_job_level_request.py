# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListJobLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobLevelRequestBuilder":
        return ListJobLevelRequestBuilder()


class ListJobLevelRequestBuilder(object):

    def __init__(self, list_job_level_request: ListJobLevelRequest = ListJobLevelRequest()) -> None:
        list_job_level_request.http_method = HttpMethod.GET
        list_job_level_request.uri = "/open-apis/corehr/v1/job_levels"
        list_job_level_request.token_types = {AccessTokenType.TENANT}
        self._list_job_level_request: ListJobLevelRequest = list_job_level_request

    def page_token(self, page_token: str) -> "ListJobLevelRequestBuilder":
        self._list_job_level_request.page_token = page_token
        self._list_job_level_request.queries["page_token"] = str(page_token)
        return self

    def page_size(self, page_size: str) -> "ListJobLevelRequestBuilder":
        self._list_job_level_request.page_size = page_size
        self._list_job_level_request.queries["page_size"] = str(page_size)
        return self

    def build(self) -> ListJobLevelRequest:
        return self._list_job_level_request
