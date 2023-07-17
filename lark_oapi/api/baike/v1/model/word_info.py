# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WordInfo(object):
    _types = {
        "input_total": int,
        "dedup_input_total": int,
        "eachday_input": List[int],
        "eachday_dedup_input": List[int],
        "send_message_total": int,
        "send_en_message_total": int,
        "receive_message_total": int,
        "receive_en_message_total": int,
        "history_words_total": int,
        "new_words_total": int,
        "eachday_send_en_message": List[int],
        "eachday_send_message": List[int],
        "eachday_receive_en_message": List[int],
        "eachday_receive_message": List[int],
        "send_eng_message_rate_ring_growth": float,
        "send_eng_words_ring_growth": int,
    }

    def __init__(self, d):
        self.input_total: Optional[int] = None
        self.dedup_input_total: Optional[int] = None
        self.eachday_input: Optional[List[int]] = None
        self.eachday_dedup_input: Optional[List[int]] = None
        self.send_message_total: Optional[int] = None
        self.send_en_message_total: Optional[int] = None
        self.receive_message_total: Optional[int] = None
        self.receive_en_message_total: Optional[int] = None
        self.history_words_total: Optional[int] = None
        self.new_words_total: Optional[int] = None
        self.eachday_send_en_message: Optional[List[int]] = None
        self.eachday_send_message: Optional[List[int]] = None
        self.eachday_receive_en_message: Optional[List[int]] = None
        self.eachday_receive_message: Optional[List[int]] = None
        self.send_eng_message_rate_ring_growth: Optional[float] = None
        self.send_eng_words_ring_growth: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WordInfoBuilder":
        return WordInfoBuilder()


class WordInfoBuilder(object):
    def __init__(self, word_info: WordInfo = WordInfo({})) -> None:
        self._word_info: WordInfo = word_info

    def input_total(self, input_total: int) -> "WordInfoBuilder":
        self._word_info.input_total = input_total
        return self

    def dedup_input_total(self, dedup_input_total: int) -> "WordInfoBuilder":
        self._word_info.dedup_input_total = dedup_input_total
        return self

    def eachday_input(self, eachday_input: List[int]) -> "WordInfoBuilder":
        self._word_info.eachday_input = eachday_input
        return self

    def eachday_dedup_input(self, eachday_dedup_input: List[int]) -> "WordInfoBuilder":
        self._word_info.eachday_dedup_input = eachday_dedup_input
        return self

    def send_message_total(self, send_message_total: int) -> "WordInfoBuilder":
        self._word_info.send_message_total = send_message_total
        return self

    def send_en_message_total(self, send_en_message_total: int) -> "WordInfoBuilder":
        self._word_info.send_en_message_total = send_en_message_total
        return self

    def receive_message_total(self, receive_message_total: int) -> "WordInfoBuilder":
        self._word_info.receive_message_total = receive_message_total
        return self

    def receive_en_message_total(self, receive_en_message_total: int) -> "WordInfoBuilder":
        self._word_info.receive_en_message_total = receive_en_message_total
        return self

    def history_words_total(self, history_words_total: int) -> "WordInfoBuilder":
        self._word_info.history_words_total = history_words_total
        return self

    def new_words_total(self, new_words_total: int) -> "WordInfoBuilder":
        self._word_info.new_words_total = new_words_total
        return self

    def eachday_send_en_message(self, eachday_send_en_message: List[int]) -> "WordInfoBuilder":
        self._word_info.eachday_send_en_message = eachday_send_en_message
        return self

    def eachday_send_message(self, eachday_send_message: List[int]) -> "WordInfoBuilder":
        self._word_info.eachday_send_message = eachday_send_message
        return self

    def eachday_receive_en_message(self, eachday_receive_en_message: List[int]) -> "WordInfoBuilder":
        self._word_info.eachday_receive_en_message = eachday_receive_en_message
        return self

    def eachday_receive_message(self, eachday_receive_message: List[int]) -> "WordInfoBuilder":
        self._word_info.eachday_receive_message = eachday_receive_message
        return self

    def send_eng_message_rate_ring_growth(self, send_eng_message_rate_ring_growth: float) -> "WordInfoBuilder":
        self._word_info.send_eng_message_rate_ring_growth = send_eng_message_rate_ring_growth
        return self

    def send_eng_words_ring_growth(self, send_eng_words_ring_growth: int) -> "WordInfoBuilder":
        self._word_info.send_eng_words_ring_growth = send_eng_words_ring_growth
        return self

    def build(self) -> "WordInfo":
        return self._word_info
