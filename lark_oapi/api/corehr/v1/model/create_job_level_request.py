# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .job_level import JobLevel


class CreateJobLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[JobLevel] = None

    @staticmethod
    def builder() -> "CreateJobLevelRequestBuilder":
        return CreateJobLevelRequestBuilder()


class CreateJobLevelRequestBuilder(object):

    def __init__(self, create_job_level_request: CreateJobLevelRequest = CreateJobLevelRequest()) -> None:
        create_job_level_request.http_method = HttpMethod.POST
        create_job_level_request.uri = "/open-apis/corehr/v1/job_levels"
        create_job_level_request.token_types = {AccessTokenType.TENANT}
        self._create_job_level_request: CreateJobLevelRequest = create_job_level_request

    def client_token(self, client_token: str) -> "CreateJobLevelRequestBuilder":
        self._create_job_level_request.client_token = client_token
        self._create_job_level_request.queries["client_token"] = str(client_token)
        return self

    def request_body(self, request_body: JobLevel) -> "CreateJobLevelRequestBuilder":
        self._create_job_level_request.request_body = request_body
        self._create_job_level_request.body = request_body
        return self

    def build(self) -> CreateJobLevelRequest:
        return self._create_job_level_request
