# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FormFieldVariableFileValue(object):
    _types = {
        "source_type": int,
        "file_id": str,
        "file_name": str,
        "length": int,
        "mime_type": str,
    }

    def __init__(self, d):
        self.source_type: Optional[int] = None
        self.file_id: Optional[str] = None
        self.file_name: Optional[str] = None
        self.length: Optional[int] = None
        self.mime_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableFileValueBuilder":
        return FormFieldVariableFileValueBuilder()


class FormFieldVariableFileValueBuilder(object):
    def __init__(self,
                 form_field_variable_file_value: FormFieldVariableFileValue = FormFieldVariableFileValue({})) -> None:
        self._form_field_variable_file_value: FormFieldVariableFileValue = form_field_variable_file_value

    def source_type(self, source_type: int) -> "FormFieldVariableFileValueBuilder":
        self._form_field_variable_file_value.source_type = source_type
        return self

    def file_id(self, file_id: str) -> "FormFieldVariableFileValueBuilder":
        self._form_field_variable_file_value.file_id = file_id
        return self

    def file_name(self, file_name: str) -> "FormFieldVariableFileValueBuilder":
        self._form_field_variable_file_value.file_name = file_name
        return self

    def length(self, length: int) -> "FormFieldVariableFileValueBuilder":
        self._form_field_variable_file_value.length = length
        return self

    def mime_type(self, mime_type: str) -> "FormFieldVariableFileValueBuilder":
        self._form_field_variable_file_value.mime_type = mime_type
        return self

    def build(self) -> "FormFieldVariableFileValue":
        return self._form_field_variable_file_value
