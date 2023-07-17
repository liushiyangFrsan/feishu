# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteProgressRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.progress_id: Optional[int] = None

    @staticmethod
    def builder() -> "DeleteProgressRecordRequestBuilder":
        return DeleteProgressRecordRequestBuilder()


class DeleteProgressRecordRequestBuilder(object):

    def __init__(self,
                 delete_progress_record_request: DeleteProgressRecordRequest = DeleteProgressRecordRequest()) -> None:
        delete_progress_record_request.http_method = HttpMethod.DELETE
        delete_progress_record_request.uri = "/open-apis/okr/v1/progress_records/:progress_id"
        delete_progress_record_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_progress_record_request: DeleteProgressRecordRequest = delete_progress_record_request

    def progress_id(self, progress_id: int) -> "DeleteProgressRecordRequestBuilder":
        self._delete_progress_record_request.progress_id = progress_id
        self._delete_progress_record_request.paths["progress_id"] = progress_id
        return self

    def build(self) -> DeleteProgressRecordRequest:
        return self._delete_progress_record_request
