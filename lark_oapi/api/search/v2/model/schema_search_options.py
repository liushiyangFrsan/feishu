# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SchemaSearchOptions(object):
    _types = {
        "enable_semantic_match": bool,
        "enable_exact_match": bool,
        "enable_prefix_match": bool,
        "enable_number_suffix_match": bool,
        "enable_camel_match": bool,
    }

    def __init__(self, d):
        self.enable_semantic_match: Optional[bool] = None
        self.enable_exact_match: Optional[bool] = None
        self.enable_prefix_match: Optional[bool] = None
        self.enable_number_suffix_match: Optional[bool] = None
        self.enable_camel_match: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SchemaSearchOptionsBuilder":
        return SchemaSearchOptionsBuilder()


class SchemaSearchOptionsBuilder(object):
    def __init__(self, schema_search_options: SchemaSearchOptions = SchemaSearchOptions({})) -> None:
        self._schema_search_options: SchemaSearchOptions = schema_search_options

    def enable_semantic_match(self, enable_semantic_match: bool) -> "SchemaSearchOptionsBuilder":
        self._schema_search_options.enable_semantic_match = enable_semantic_match
        return self

    def enable_exact_match(self, enable_exact_match: bool) -> "SchemaSearchOptionsBuilder":
        self._schema_search_options.enable_exact_match = enable_exact_match
        return self

    def enable_prefix_match(self, enable_prefix_match: bool) -> "SchemaSearchOptionsBuilder":
        self._schema_search_options.enable_prefix_match = enable_prefix_match
        return self

    def enable_number_suffix_match(self, enable_number_suffix_match: bool) -> "SchemaSearchOptionsBuilder":
        self._schema_search_options.enable_number_suffix_match = enable_number_suffix_match
        return self

    def enable_camel_match(self, enable_camel_match: bool) -> "SchemaSearchOptionsBuilder":
        self._schema_search_options.enable_camel_match = enable_camel_match
        return self

    def build(self) -> "SchemaSearchOptions":
        return self._schema_search_options
