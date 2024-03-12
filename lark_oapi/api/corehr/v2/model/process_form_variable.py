# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .form_variable_value_info import FormVariableValueInfo


class ProcessFormVariable(object):
    _types = {
        "variable_api_name": str,
        "variable_value": FormVariableValueInfo,
    }

    def __init__(self, d=None):
        self.variable_api_name: Optional[str] = None
        self.variable_value: Optional[FormVariableValueInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProcessFormVariableBuilder":
        return ProcessFormVariableBuilder()


class ProcessFormVariableBuilder(object):
    def __init__(self) -> None:
        self._process_form_variable = ProcessFormVariable()

    def variable_api_name(self, variable_api_name: str) -> "ProcessFormVariableBuilder":
        self._process_form_variable.variable_api_name = variable_api_name
        return self

    def variable_value(self, variable_value: FormVariableValueInfo) -> "ProcessFormVariableBuilder":
        self._process_form_variable.variable_value = variable_value
        return self

    def build(self) -> "ProcessFormVariable":
        return self._process_form_variable