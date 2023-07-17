# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .file import File
from .instance_cc_user import InstanceCcUser


class InstanceTimeline(object):
    _types = {
        "type": str,
        "create_time": int,
        "user_id": str,
        "open_id": str,
        "user_id_list": List[str],
        "open_id_list": List[str],
        "task_id": str,
        "comment": str,
        "cc_user_list": List[InstanceCcUser],
        "ext": str,
        "node_key": str,
        "files": List[File],
    }

    def __init__(self, d):
        self.type: Optional[str] = None
        self.create_time: Optional[int] = None
        self.user_id: Optional[str] = None
        self.open_id: Optional[str] = None
        self.user_id_list: Optional[List[str]] = None
        self.open_id_list: Optional[List[str]] = None
        self.task_id: Optional[str] = None
        self.comment: Optional[str] = None
        self.cc_user_list: Optional[List[InstanceCcUser]] = None
        self.ext: Optional[str] = None
        self.node_key: Optional[str] = None
        self.files: Optional[List[File]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceTimelineBuilder":
        return InstanceTimelineBuilder()


class InstanceTimelineBuilder(object):
    def __init__(self, instance_timeline: InstanceTimeline = InstanceTimeline({})) -> None:
        self._instance_timeline: InstanceTimeline = instance_timeline

    def type(self, type: str) -> "InstanceTimelineBuilder":
        self._instance_timeline.type = type
        return self

    def create_time(self, create_time: int) -> "InstanceTimelineBuilder":
        self._instance_timeline.create_time = create_time
        return self

    def user_id(self, user_id: str) -> "InstanceTimelineBuilder":
        self._instance_timeline.user_id = user_id
        return self

    def open_id(self, open_id: str) -> "InstanceTimelineBuilder":
        self._instance_timeline.open_id = open_id
        return self

    def user_id_list(self, user_id_list: List[str]) -> "InstanceTimelineBuilder":
        self._instance_timeline.user_id_list = user_id_list
        return self

    def open_id_list(self, open_id_list: List[str]) -> "InstanceTimelineBuilder":
        self._instance_timeline.open_id_list = open_id_list
        return self

    def task_id(self, task_id: str) -> "InstanceTimelineBuilder":
        self._instance_timeline.task_id = task_id
        return self

    def comment(self, comment: str) -> "InstanceTimelineBuilder":
        self._instance_timeline.comment = comment
        return self

    def cc_user_list(self, cc_user_list: List[InstanceCcUser]) -> "InstanceTimelineBuilder":
        self._instance_timeline.cc_user_list = cc_user_list
        return self

    def ext(self, ext: str) -> "InstanceTimelineBuilder":
        self._instance_timeline.ext = ext
        return self

    def node_key(self, node_key: str) -> "InstanceTimelineBuilder":
        self._instance_timeline.node_key = node_key
        return self

    def files(self, files: List[File]) -> "InstanceTimelineBuilder":
        self._instance_timeline.files = files
        return self

    def build(self) -> "InstanceTimeline":
        return self._instance_timeline
