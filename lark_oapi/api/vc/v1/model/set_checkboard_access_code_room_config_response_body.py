# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SetCheckboardAccessCodeRoomConfigResponseBody(object):
    _types = {
        "access_code": str,
    }

    def __init__(self, d):
        self.access_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SetCheckboardAccessCodeRoomConfigResponseBodyBuilder":
        return SetCheckboardAccessCodeRoomConfigResponseBodyBuilder()


class SetCheckboardAccessCodeRoomConfigResponseBodyBuilder(object):
    def __init__(self,
                 set_checkboard_access_code_room_config_response_body: SetCheckboardAccessCodeRoomConfigResponseBody = SetCheckboardAccessCodeRoomConfigResponseBody(
                     {})) -> None:
        self._set_checkboard_access_code_room_config_response_body: SetCheckboardAccessCodeRoomConfigResponseBody = set_checkboard_access_code_room_config_response_body

    def access_code(self, access_code: str) -> "SetCheckboardAccessCodeRoomConfigResponseBodyBuilder":
        self._set_checkboard_access_code_room_config_response_body.access_code = access_code
        return self

    def build(self) -> "SetCheckboardAccessCodeRoomConfigResponseBody":
        return self._set_checkboard_access_code_room_config_response_body
