# Code generated by Lark OpenAPI.

from .v1.resource import *


class OkrService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)


class V1(object):
    def __init__(self, config: Config) -> None:
        self.image: Optional[Image] = Image(config)
        self.metric_source: Optional[MetricSource] = MetricSource(config)
        self.metric_source_table: Optional[MetricSourceTable] = MetricSourceTable(config)
        self.metric_source_table_item: Optional[MetricSourceTableItem] = MetricSourceTableItem(config)
        self.okr: Optional[Okr] = Okr(config)
        self.period: Optional[Period] = Period(config)
        self.progress_record: Optional[ProgressRecord] = ProgressRecord(config)
        self.user_okr: Optional[UserOkr] = UserOkr(config)
