# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApplicationTalentCompetitionInfo(object):
    _types = {
        "id": str,
        "name": str,
        "desc": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.desc: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationTalentCompetitionInfoBuilder":
        return ApplicationTalentCompetitionInfoBuilder()


class ApplicationTalentCompetitionInfoBuilder(object):
    def __init__(self,
                 application_talent_competition_info: ApplicationTalentCompetitionInfo = ApplicationTalentCompetitionInfo(
                     {})) -> None:
        self._application_talent_competition_info: ApplicationTalentCompetitionInfo = application_talent_competition_info

    def id(self, id: str) -> "ApplicationTalentCompetitionInfoBuilder":
        self._application_talent_competition_info.id = id
        return self

    def name(self, name: str) -> "ApplicationTalentCompetitionInfoBuilder":
        self._application_talent_competition_info.name = name
        return self

    def desc(self, desc: str) -> "ApplicationTalentCompetitionInfoBuilder":
        self._application_talent_competition_info.desc = desc
        return self

    def build(self) -> "ApplicationTalentCompetitionInfo":
        return self._application_talent_competition_info
