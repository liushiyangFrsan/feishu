# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class ObjectAttribute(object):
    _types = {
        "title": I18n,
        "description": I18n,
        "data_type": int,
        "tags": List[int],
        "is_fcf_data": bool,
        "is_di_data": bool,
    }

    def __init__(self, d):
        self.title: Optional[I18n] = None
        self.description: Optional[I18n] = None
        self.data_type: Optional[int] = None
        self.tags: Optional[List[int]] = None
        self.is_fcf_data: Optional[bool] = None
        self.is_di_data: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ObjectAttributeBuilder":
        return ObjectAttributeBuilder()


class ObjectAttributeBuilder(object):
    def __init__(self, object_attribute: ObjectAttribute = ObjectAttribute({})) -> None:
        self._object_attribute: ObjectAttribute = object_attribute

    def title(self, title: I18n) -> "ObjectAttributeBuilder":
        self._object_attribute.title = title
        return self

    def description(self, description: I18n) -> "ObjectAttributeBuilder":
        self._object_attribute.description = description
        return self

    def data_type(self, data_type: int) -> "ObjectAttributeBuilder":
        self._object_attribute.data_type = data_type
        return self

    def tags(self, tags: List[int]) -> "ObjectAttributeBuilder":
        self._object_attribute.tags = tags
        return self

    def is_fcf_data(self, is_fcf_data: bool) -> "ObjectAttributeBuilder":
        self._object_attribute.is_fcf_data = is_fcf_data
        return self

    def is_di_data(self, is_di_data: bool) -> "ObjectAttributeBuilder":
        self._object_attribute.is_di_data = is_di_data
        return self

    def build(self) -> "ObjectAttribute":
        return self._object_attribute