# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class TransferType(object):
    _types = {
        "transfer_type_unique_identifier": str,
        "name": List[I18n],
        "active": bool,
        "flow_id": str,
        "flow_name": List[I18n],
        "created_time": str,
        "updated_time": str,
    }

    def __init__(self, d):
        self.transfer_type_unique_identifier: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.active: Optional[bool] = None
        self.flow_id: Optional[str] = None
        self.flow_name: Optional[List[I18n]] = None
        self.created_time: Optional[str] = None
        self.updated_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TransferTypeBuilder":
        return TransferTypeBuilder()


class TransferTypeBuilder(object):
    def __init__(self, transfer_type: TransferType = TransferType({})) -> None:
        self._transfer_type: TransferType = transfer_type

    def transfer_type_unique_identifier(self, transfer_type_unique_identifier: str) -> "TransferTypeBuilder":
        self._transfer_type.transfer_type_unique_identifier = transfer_type_unique_identifier
        return self

    def name(self, name: List[I18n]) -> "TransferTypeBuilder":
        self._transfer_type.name = name
        return self

    def active(self, active: bool) -> "TransferTypeBuilder":
        self._transfer_type.active = active
        return self

    def flow_id(self, flow_id: str) -> "TransferTypeBuilder":
        self._transfer_type.flow_id = flow_id
        return self

    def flow_name(self, flow_name: List[I18n]) -> "TransferTypeBuilder":
        self._transfer_type.flow_name = flow_name
        return self

    def created_time(self, created_time: str) -> "TransferTypeBuilder":
        self._transfer_type.created_time = created_time
        return self

    def updated_time(self, updated_time: str) -> "TransferTypeBuilder":
        self._transfer_type.updated_time = updated_time
        return self

    def build(self) -> "TransferType":
        return self._transfer_type
