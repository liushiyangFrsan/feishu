# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .question import Question


class Questionnaire(object):
    _types = {
        "questionnaire_id": str,
        "application_id": str,
        "interview_id": str,
        "version": int,
        "questions": List[Question],
        "has_answers": bool,
        "update_time": str,
    }

    def __init__(self, d):
        self.questionnaire_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.interview_id: Optional[str] = None
        self.version: Optional[int] = None
        self.questions: Optional[List[Question]] = None
        self.has_answers: Optional[bool] = None
        self.update_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QuestionnaireBuilder":
        return QuestionnaireBuilder()


class QuestionnaireBuilder(object):
    def __init__(self, questionnaire: Questionnaire = Questionnaire({})) -> None:
        self._questionnaire: Questionnaire = questionnaire

    def questionnaire_id(self, questionnaire_id: str) -> "QuestionnaireBuilder":
        self._questionnaire.questionnaire_id = questionnaire_id
        return self

    def application_id(self, application_id: str) -> "QuestionnaireBuilder":
        self._questionnaire.application_id = application_id
        return self

    def interview_id(self, interview_id: str) -> "QuestionnaireBuilder":
        self._questionnaire.interview_id = interview_id
        return self

    def version(self, version: int) -> "QuestionnaireBuilder":
        self._questionnaire.version = version
        return self

    def questions(self, questions: List[Question]) -> "QuestionnaireBuilder":
        self._questionnaire.questions = questions
        return self

    def has_answers(self, has_answers: bool) -> "QuestionnaireBuilder":
        self._questionnaire.has_answers = has_answers
        return self

    def update_time(self, update_time: str) -> "QuestionnaireBuilder":
        self._questionnaire.update_time = update_time
        return self

    def build(self) -> "Questionnaire":
        return self._questionnaire
