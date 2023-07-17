# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class QueryUserStatsDataRequestBody(object):
    _types = {
        "locale": str,
        "stats_type": str,
        "start_date": int,
        "end_date": int,
        "user_ids": List[str],
        "need_history": bool,
        "current_group_only": bool,
        "user_id": str,
    }

    def __init__(self, d):
        self.locale: Optional[str] = None
        self.stats_type: Optional[str] = None
        self.start_date: Optional[int] = None
        self.end_date: Optional[int] = None
        self.user_ids: Optional[List[str]] = None
        self.need_history: Optional[bool] = None
        self.current_group_only: Optional[bool] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserStatsDataRequestBodyBuilder":
        return QueryUserStatsDataRequestBodyBuilder()


class QueryUserStatsDataRequestBodyBuilder(object):
    def __init__(self,
                 query_user_stats_data_request_body: QueryUserStatsDataRequestBody = QueryUserStatsDataRequestBody(
                     {})) -> None:
        self._query_user_stats_data_request_body: QueryUserStatsDataRequestBody = query_user_stats_data_request_body

    def locale(self, locale: str) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.locale = locale
        return self

    def stats_type(self, stats_type: str) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.stats_type = stats_type
        return self

    def start_date(self, start_date: int) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.start_date = start_date
        return self

    def end_date(self, end_date: int) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.end_date = end_date
        return self

    def user_ids(self, user_ids: List[str]) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.user_ids = user_ids
        return self

    def need_history(self, need_history: bool) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.need_history = need_history
        return self

    def current_group_only(self, current_group_only: bool) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.current_group_only = current_group_only
        return self

    def user_id(self, user_id: str) -> "QueryUserStatsDataRequestBodyBuilder":
        self._query_user_stats_data_request_body.user_id = user_id
        return self

    def build(self) -> "QueryUserStatsDataRequestBody":
        return self._query_user_stats_data_request_body
