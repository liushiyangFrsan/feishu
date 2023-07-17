# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .entity import Entity


class UpdateEntityResponseBody(object):
    _types = {
        "entity": Entity,
    }

    def __init__(self, d):
        self.entity: Optional[Entity] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateEntityResponseBodyBuilder":
        return UpdateEntityResponseBodyBuilder()


class UpdateEntityResponseBodyBuilder(object):
    def __init__(self, update_entity_response_body: UpdateEntityResponseBody = UpdateEntityResponseBody({})) -> None:
        self._update_entity_response_body: UpdateEntityResponseBody = update_entity_response_body

    def entity(self, entity: Entity) -> "UpdateEntityResponseBodyBuilder":
        self._update_entity_response_body.entity = entity
        return self

    def build(self) -> "UpdateEntityResponseBody":
        return self._update_entity_response_body
