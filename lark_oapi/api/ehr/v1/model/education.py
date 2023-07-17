# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Education(object):
    _types = {
        "level": int,
        "school": str,
        "major": str,
        "degree": int,
        "start": str,
        "end": str,
    }

    def __init__(self, d):
        self.level: Optional[int] = None
        self.school: Optional[str] = None
        self.major: Optional[str] = None
        self.degree: Optional[int] = None
        self.start: Optional[str] = None
        self.end: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EducationBuilder":
        return EducationBuilder()


class EducationBuilder(object):
    def __init__(self, education: Education = Education({})) -> None:
        self._education: Education = education

    def level(self, level: int) -> "EducationBuilder":
        self._education.level = level
        return self

    def school(self, school: str) -> "EducationBuilder":
        self._education.school = school
        return self

    def major(self, major: str) -> "EducationBuilder":
        self._education.major = major
        return self

    def degree(self, degree: int) -> "EducationBuilder":
        self._education.degree = degree
        return self

    def start(self, start: str) -> "EducationBuilder":
        self._education.start = start
        return self

    def end(self, end: str) -> "EducationBuilder":
        self._education.end = end
        return self

    def build(self) -> "Education":
        return self._education
