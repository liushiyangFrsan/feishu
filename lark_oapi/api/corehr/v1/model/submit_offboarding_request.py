# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .submit_offboarding_request_body import SubmitOffboardingRequestBody


class SubmitOffboardingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[SubmitOffboardingRequestBody] = None

    @staticmethod
    def builder() -> "SubmitOffboardingRequestBuilder":
        return SubmitOffboardingRequestBuilder()


class SubmitOffboardingRequestBuilder(object):

    def __init__(self, submit_offboarding_request: SubmitOffboardingRequest = SubmitOffboardingRequest()) -> None:
        submit_offboarding_request.http_method = HttpMethod.POST
        submit_offboarding_request.uri = "/open-apis/corehr/v1/offboardings/submit"
        submit_offboarding_request.token_types = {AccessTokenType.TENANT}
        self._submit_offboarding_request: SubmitOffboardingRequest = submit_offboarding_request

    def user_id_type(self, user_id_type: str) -> "SubmitOffboardingRequestBuilder":
        self._submit_offboarding_request.user_id_type = user_id_type
        self._submit_offboarding_request.queries["user_id_type"] = str(user_id_type)
        return self

    def request_body(self, request_body: SubmitOffboardingRequestBody) -> "SubmitOffboardingRequestBuilder":
        self._submit_offboarding_request.request_body = request_body
        self._submit_offboarding_request.body = request_body
        return self

    def build(self) -> SubmitOffboardingRequest:
        return self._submit_offboarding_request
