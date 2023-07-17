# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Note(object):
    _types = {
        "id": str,
        "talent_id": str,
        "application_id": str,
        "is_private": bool,
        "create_time": int,
        "modify_time": int,
        "creator_id": str,
        "content": str,
        "privacy": int,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.is_private: Optional[bool] = None
        self.create_time: Optional[int] = None
        self.modify_time: Optional[int] = None
        self.creator_id: Optional[str] = None
        self.content: Optional[str] = None
        self.privacy: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NoteBuilder":
        return NoteBuilder()


class NoteBuilder(object):
    def __init__(self, note: Note = Note({})) -> None:
        self._note: Note = note

    def id(self, id: str) -> "NoteBuilder":
        self._note.id = id
        return self

    def talent_id(self, talent_id: str) -> "NoteBuilder":
        self._note.talent_id = talent_id
        return self

    def application_id(self, application_id: str) -> "NoteBuilder":
        self._note.application_id = application_id
        return self

    def is_private(self, is_private: bool) -> "NoteBuilder":
        self._note.is_private = is_private
        return self

    def create_time(self, create_time: int) -> "NoteBuilder":
        self._note.create_time = create_time
        return self

    def modify_time(self, modify_time: int) -> "NoteBuilder":
        self._note.modify_time = modify_time
        return self

    def creator_id(self, creator_id: str) -> "NoteBuilder":
        self._note.creator_id = creator_id
        return self

    def content(self, content: str) -> "NoteBuilder":
        self._note.content = content
        return self

    def privacy(self, privacy: int) -> "NoteBuilder":
        self._note.privacy = privacy
        return self

    def build(self) -> "Note":
        return self._note
