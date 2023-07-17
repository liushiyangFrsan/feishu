# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateInstanceResponseBody(object):
    _types = {
        "instance_code": str,
    }

    def __init__(self, d):
        self.instance_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateInstanceResponseBodyBuilder":
        return CreateInstanceResponseBodyBuilder()


class CreateInstanceResponseBodyBuilder(object):
    def __init__(self,
                 create_instance_response_body: CreateInstanceResponseBody = CreateInstanceResponseBody({})) -> None:
        self._create_instance_response_body: CreateInstanceResponseBody = create_instance_response_body

    def instance_code(self, instance_code: str) -> "CreateInstanceResponseBodyBuilder":
        self._create_instance_response_body.instance_code = instance_code
        return self

    def build(self) -> "CreateInstanceResponseBody":
        return self._create_instance_response_body
