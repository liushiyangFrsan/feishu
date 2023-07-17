# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .okr_objective_aligned_objective_owner import OkrObjectiveAlignedObjectiveOwner


class OkrComment(object):
    _types = {
        "id": int,
        "content": str,
        "comment_time": int,
        "commentator": OkrObjectiveAlignedObjectiveOwner,
        "last_modifier": OkrObjectiveAlignedObjectiveOwner,
        "content_modify_time": int,
        "solved_time": int,
    }

    def __init__(self, d):
        self.id: Optional[int] = None
        self.content: Optional[str] = None
        self.comment_time: Optional[int] = None
        self.commentator: Optional[OkrObjectiveAlignedObjectiveOwner] = None
        self.last_modifier: Optional[OkrObjectiveAlignedObjectiveOwner] = None
        self.content_modify_time: Optional[int] = None
        self.solved_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrCommentBuilder":
        return OkrCommentBuilder()


class OkrCommentBuilder(object):
    def __init__(self, okr_comment: OkrComment = OkrComment({})) -> None:
        self._okr_comment: OkrComment = okr_comment

    def id(self, id: int) -> "OkrCommentBuilder":
        self._okr_comment.id = id
        return self

    def content(self, content: str) -> "OkrCommentBuilder":
        self._okr_comment.content = content
        return self

    def comment_time(self, comment_time: int) -> "OkrCommentBuilder":
        self._okr_comment.comment_time = comment_time
        return self

    def commentator(self, commentator: OkrObjectiveAlignedObjectiveOwner) -> "OkrCommentBuilder":
        self._okr_comment.commentator = commentator
        return self

    def last_modifier(self, last_modifier: OkrObjectiveAlignedObjectiveOwner) -> "OkrCommentBuilder":
        self._okr_comment.last_modifier = last_modifier
        return self

    def content_modify_time(self, content_modify_time: int) -> "OkrCommentBuilder":
        self._okr_comment.content_modify_time = content_modify_time
        return self

    def solved_time(self, solved_time: int) -> "OkrCommentBuilder":
        self._okr_comment.solved_time = solved_time
        return self

    def build(self) -> "OkrComment":
        return self._okr_comment
