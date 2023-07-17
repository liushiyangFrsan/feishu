# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .category import Category
from .richtext import Richtext
from .ticket_user import TicketUser


class Faq(object):
    _types = {
        "faq_id": str,
        "id": str,
        "helpdesk_id": str,
        "question": str,
        "answer": str,
        "answer_richtext": List[Richtext],
        "create_time": int,
        "update_time": int,
        "categories": List[Category],
        "tags": List[str],
        "expire_time": int,
        "update_user": TicketUser,
        "create_user": TicketUser,
    }

    def __init__(self, d):
        self.faq_id: Optional[str] = None
        self.id: Optional[str] = None
        self.helpdesk_id: Optional[str] = None
        self.question: Optional[str] = None
        self.answer: Optional[str] = None
        self.answer_richtext: Optional[List[Richtext]] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.categories: Optional[List[Category]] = None
        self.tags: Optional[List[str]] = None
        self.expire_time: Optional[int] = None
        self.update_user: Optional[TicketUser] = None
        self.create_user: Optional[TicketUser] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FaqBuilder":
        return FaqBuilder()


class FaqBuilder(object):
    def __init__(self, faq: Faq = Faq({})) -> None:
        self._faq: Faq = faq

    def faq_id(self, faq_id: str) -> "FaqBuilder":
        self._faq.faq_id = faq_id
        return self

    def id(self, id: str) -> "FaqBuilder":
        self._faq.id = id
        return self

    def helpdesk_id(self, helpdesk_id: str) -> "FaqBuilder":
        self._faq.helpdesk_id = helpdesk_id
        return self

    def question(self, question: str) -> "FaqBuilder":
        self._faq.question = question
        return self

    def answer(self, answer: str) -> "FaqBuilder":
        self._faq.answer = answer
        return self

    def answer_richtext(self, answer_richtext: List[Richtext]) -> "FaqBuilder":
        self._faq.answer_richtext = answer_richtext
        return self

    def create_time(self, create_time: int) -> "FaqBuilder":
        self._faq.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "FaqBuilder":
        self._faq.update_time = update_time
        return self

    def categories(self, categories: List[Category]) -> "FaqBuilder":
        self._faq.categories = categories
        return self

    def tags(self, tags: List[str]) -> "FaqBuilder":
        self._faq.tags = tags
        return self

    def expire_time(self, expire_time: int) -> "FaqBuilder":
        self._faq.expire_time = expire_time
        return self

    def update_user(self, update_user: TicketUser) -> "FaqBuilder":
        self._faq.update_user = update_user
        return self

    def create_user(self, create_user: TicketUser) -> "FaqBuilder":
        self._faq.create_user = create_user
        return self

    def build(self) -> "Faq":
        return self._faq
