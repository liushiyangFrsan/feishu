# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .data_validation_rule import DataValidationRule


class DataValidation(object):
    _types = {
        "data_validation_id": int,
        "data_validation_rule": DataValidationRule,
        "strict": str,
        "help_text": str,
    }

    def __init__(self, d):
        self.data_validation_id: Optional[int] = None
        self.data_validation_rule: Optional[DataValidationRule] = None
        self.strict: Optional[str] = None
        self.help_text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DataValidationBuilder":
        return DataValidationBuilder()


class DataValidationBuilder(object):
    def __init__(self, data_validation: DataValidation = DataValidation({})) -> None:
        self._data_validation: DataValidation = data_validation

    def data_validation_id(self, data_validation_id: int) -> "DataValidationBuilder":
        self._data_validation.data_validation_id = data_validation_id
        return self

    def data_validation_rule(self, data_validation_rule: DataValidationRule) -> "DataValidationBuilder":
        self._data_validation.data_validation_rule = data_validation_rule
        return self

    def strict(self, strict: str) -> "DataValidationBuilder":
        self._data_validation.strict = strict
        return self

    def help_text(self, help_text: str) -> "DataValidationBuilder":
        self._data_validation.help_text = help_text
        return self

    def build(self) -> "DataValidation":
        return self._data_validation
