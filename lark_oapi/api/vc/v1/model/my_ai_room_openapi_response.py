# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiRoomOpenapiResponse(object):
    _types = {
        "response_type": int,
        "schedule_event_id": str,
    }

    def __init__(self, d=None):
        self.response_type: Optional[int] = None
        self.schedule_event_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiRoomOpenapiResponseBuilder":
        return MyAiRoomOpenapiResponseBuilder()


class MyAiRoomOpenapiResponseBuilder(object):
    def __init__(self) -> None:
        self._my_ai_room_openapi_response = MyAiRoomOpenapiResponse()

    def response_type(self, response_type: int) -> "MyAiRoomOpenapiResponseBuilder":
        self._my_ai_room_openapi_response.response_type = response_type
        return self

    def schedule_event_id(self, schedule_event_id: str) -> "MyAiRoomOpenapiResponseBuilder":
        self._my_ai_room_openapi_response.schedule_event_id = schedule_event_id
        return self

    def build(self) -> "MyAiRoomOpenapiResponse":
        return self._my_ai_room_openapi_response