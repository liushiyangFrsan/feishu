# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .id_name_object import IdNameObject


class TalentOperationLog(object):
    _types = {
        "application_id": str,
        "talent_id": str,
        "operator": IdNameObject,
        "operation_type": int,
        "operation_time": str,
        "operator_type": int,
    }

    def __init__(self, d):
        self.application_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.operator: Optional[IdNameObject] = None
        self.operation_type: Optional[int] = None
        self.operation_time: Optional[str] = None
        self.operator_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentOperationLogBuilder":
        return TalentOperationLogBuilder()


class TalentOperationLogBuilder(object):
    def __init__(self, talent_operation_log: TalentOperationLog = TalentOperationLog({})) -> None:
        self._talent_operation_log: TalentOperationLog = talent_operation_log

    def application_id(self, application_id: str) -> "TalentOperationLogBuilder":
        self._talent_operation_log.application_id = application_id
        return self

    def talent_id(self, talent_id: str) -> "TalentOperationLogBuilder":
        self._talent_operation_log.talent_id = talent_id
        return self

    def operator(self, operator: IdNameObject) -> "TalentOperationLogBuilder":
        self._talent_operation_log.operator = operator
        return self

    def operation_type(self, operation_type: int) -> "TalentOperationLogBuilder":
        self._talent_operation_log.operation_type = operation_type
        return self

    def operation_time(self, operation_time: str) -> "TalentOperationLogBuilder":
        self._talent_operation_log.operation_time = operation_time
        return self

    def operator_type(self, operator_type: int) -> "TalentOperationLogBuilder":
        self._talent_operation_log.operator_type = operator_type
        return self

    def build(self) -> "TalentOperationLog":
        return self._talent_operation_log
