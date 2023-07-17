# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_create_user_daily_shift_request_body import BatchCreateUserDailyShiftRequestBody


class BatchCreateUserDailyShiftRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.request_body: Optional[BatchCreateUserDailyShiftRequestBody] = None

    @staticmethod
    def builder() -> "BatchCreateUserDailyShiftRequestBuilder":
        return BatchCreateUserDailyShiftRequestBuilder()


class BatchCreateUserDailyShiftRequestBuilder(object):

    def __init__(self,
                 batch_create_user_daily_shift_request: BatchCreateUserDailyShiftRequest = BatchCreateUserDailyShiftRequest()) -> None:
        batch_create_user_daily_shift_request.http_method = HttpMethod.POST
        batch_create_user_daily_shift_request.uri = "/open-apis/attendance/v1/user_daily_shifts/batch_create"
        batch_create_user_daily_shift_request.token_types = {AccessTokenType.TENANT}
        self._batch_create_user_daily_shift_request: BatchCreateUserDailyShiftRequest = batch_create_user_daily_shift_request

    def employee_type(self, employee_type: str) -> "BatchCreateUserDailyShiftRequestBuilder":
        self._batch_create_user_daily_shift_request.employee_type = employee_type
        self._batch_create_user_daily_shift_request.queries["employee_type"] = str(employee_type)
        return self

    def request_body(self,
                     request_body: BatchCreateUserDailyShiftRequestBody) -> "BatchCreateUserDailyShiftRequestBuilder":
        self._batch_create_user_daily_shift_request.request_body = request_body
        self._batch_create_user_daily_shift_request.body = request_body
        return self

    def build(self) -> BatchCreateUserDailyShiftRequest:
        return self._batch_create_user_daily_shift_request
