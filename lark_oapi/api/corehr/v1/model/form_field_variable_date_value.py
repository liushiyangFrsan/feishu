# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FormFieldVariableDateValue(object):
    _types = {
        "value": int,
    }

    def __init__(self, d):
        self.value: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableDateValueBuilder":
        return FormFieldVariableDateValueBuilder()


class FormFieldVariableDateValueBuilder(object):
    def __init__(self,
                 form_field_variable_date_value: FormFieldVariableDateValue = FormFieldVariableDateValue({})) -> None:
        self._form_field_variable_date_value: FormFieldVariableDateValue = form_field_variable_date_value

    def value(self, value: int) -> "FormFieldVariableDateValueBuilder":
        self._form_field_variable_date_value.value = value
        return self

    def build(self) -> "FormFieldVariableDateValue":
        return self._form_field_variable_date_value
