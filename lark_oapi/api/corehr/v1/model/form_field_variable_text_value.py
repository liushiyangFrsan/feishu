# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FormFieldVariableTextValue(object):
    _types = {
        "value": str,
    }

    def __init__(self, d):
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableTextValueBuilder":
        return FormFieldVariableTextValueBuilder()


class FormFieldVariableTextValueBuilder(object):
    def __init__(self,
                 form_field_variable_text_value: FormFieldVariableTextValue = FormFieldVariableTextValue({})) -> None:
        self._form_field_variable_text_value: FormFieldVariableTextValue = form_field_variable_text_value

    def value(self, value: str) -> "FormFieldVariableTextValueBuilder":
        self._form_field_variable_text_value.value = value
        return self

    def build(self) -> "FormFieldVariableTextValue":
        return self._form_field_variable_text_value
