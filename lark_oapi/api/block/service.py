# Code generated by Lark OpenAPI.

from .v2.resource import *


class BlockService(object):
    def __init__(self, config: Config) -> None:
        self.v2: V2 = V2(config)


class V2(object):
    def __init__(self, config: Config) -> None:
        self.entity: Optional[Entity] = Entity(config)
        self.message: Optional[Message] = Message(config)
