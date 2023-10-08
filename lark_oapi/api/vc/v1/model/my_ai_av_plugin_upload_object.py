# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiAvPluginUploadObject(object):
    _types = {
        "biz_id": str,
        "type": str,
    }

    def __init__(self, d=None):
        self.biz_id: Optional[str] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiAvPluginUploadObjectBuilder":
        return MyAiAvPluginUploadObjectBuilder()


class MyAiAvPluginUploadObjectBuilder(object):
    def __init__(self) -> None:
        self._my_ai_av_plugin_upload_object = MyAiAvPluginUploadObject()

    def biz_id(self, biz_id: str) -> "MyAiAvPluginUploadObjectBuilder":
        self._my_ai_av_plugin_upload_object.biz_id = biz_id
        return self

    def type(self, type: str) -> "MyAiAvPluginUploadObjectBuilder":
        self._my_ai_av_plugin_upload_object.type = type
        return self

    def build(self) -> "MyAiAvPluginUploadObject":
        return self._my_ai_av_plugin_upload_object