# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .file import File


class FileList(object):
    _types = {
        "files": List[File],
    }

    def __init__(self, d):
        self.files: Optional[List[File]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileListBuilder":
        return FileListBuilder()


class FileListBuilder(object):
    def __init__(self, file_list: FileList = FileList({})) -> None:
        self._file_list: FileList = file_list

    def files(self, files: List[File]) -> "FileListBuilder":
        self._file_list.files = files
        return self

    def build(self) -> "FileList":
        return self._file_list
