# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .meeting_settings import MeetingSettings
from .vc_info import VcInfo


class Vchat(object):
    _types = {
        "vc_type": str,
        "icon_type": str,
        "description": str,
        "meeting_url": str,
        "meeting_settings": MeetingSettings,
    }

    def __init__(self, d):
        self.vc_type: Optional[str] = None
        self.icon_type: Optional[str] = None
        self.description: Optional[str] = None
        self.meeting_url: Optional[str] = None
        self.live_link: Optional[str] = None
        self.vc_info: Optional[VcInfo] = None
        self.meeting_settings: Optional[MeetingSettings] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VchatBuilder":
        return VchatBuilder()


class VchatBuilder(object):
    def __init__(self, vchat: Vchat = Vchat({})) -> None:
        self._vchat: Vchat = vchat

    def vc_type(self, vc_type: str) -> "VchatBuilder":
        self._vchat.vc_type = vc_type
        return self

    def icon_type(self, icon_type: str) -> "VchatBuilder":
        self._vchat.icon_type = icon_type
        return self

    def description(self, description: str) -> "VchatBuilder":
        self._vchat.description = description
        return self

    def meeting_url(self, meeting_url: str) -> "VchatBuilder":
        self._vchat.meeting_url = meeting_url
        return self

    def meeting_settings(self, meeting_settings: MeetingSettings) -> "VchatBuilder":
        self._vchat.meeting_settings = meeting_settings
        return self

    def build(self) -> "Vchat":
        return self._vchat
