# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table_record import AppTableRecord


class UpdateAppTableRecordResponseBody(object):
    _types = {
        "record": AppTableRecord,
    }

    def __init__(self, d):
        self.record: Optional[AppTableRecord] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateAppTableRecordResponseBodyBuilder":
        return UpdateAppTableRecordResponseBodyBuilder()


class UpdateAppTableRecordResponseBodyBuilder(object):
    def __init__(self,
                 update_app_table_record_response_body: UpdateAppTableRecordResponseBody = UpdateAppTableRecordResponseBody(
                     {})) -> None:
        self._update_app_table_record_response_body: UpdateAppTableRecordResponseBody = update_app_table_record_response_body

    def record(self, record: AppTableRecord) -> "UpdateAppTableRecordResponseBodyBuilder":
        self._update_app_table_record_response_body.record = record
        return self

    def build(self) -> "UpdateAppTableRecordResponseBody":
        return self._update_app_table_record_response_body
