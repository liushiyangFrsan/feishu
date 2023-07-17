# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class TalentSchema(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentSchemaBuilder":
        return TalentSchemaBuilder()


class TalentSchemaBuilder(object):
    def __init__(self, talent_schema: TalentSchema = TalentSchema({})) -> None:
        self._talent_schema: TalentSchema = talent_schema

    def build(self) -> "TalentSchema":
        return self._talent_schema
