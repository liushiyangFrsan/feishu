# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class QualityCpuUsage(object):
    _types = {
        "time": str,
        "client_avg_cpu_usage": str,
        "client_max_cpu_usage": str,
        "system_avg_cpu_usage": str,
        "system_max_cpu_usage": str,
    }

    def __init__(self, d):
        self.time: Optional[str] = None
        self.client_avg_cpu_usage: Optional[str] = None
        self.client_max_cpu_usage: Optional[str] = None
        self.system_avg_cpu_usage: Optional[str] = None
        self.system_max_cpu_usage: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QualityCpuUsageBuilder":
        return QualityCpuUsageBuilder()


class QualityCpuUsageBuilder(object):
    def __init__(self, quality_cpu_usage: QualityCpuUsage = QualityCpuUsage({})) -> None:
        self._quality_cpu_usage: QualityCpuUsage = quality_cpu_usage

    def time(self, time: str) -> "QualityCpuUsageBuilder":
        self._quality_cpu_usage.time = time
        return self

    def client_avg_cpu_usage(self, client_avg_cpu_usage: str) -> "QualityCpuUsageBuilder":
        self._quality_cpu_usage.client_avg_cpu_usage = client_avg_cpu_usage
        return self

    def client_max_cpu_usage(self, client_max_cpu_usage: str) -> "QualityCpuUsageBuilder":
        self._quality_cpu_usage.client_max_cpu_usage = client_max_cpu_usage
        return self

    def system_avg_cpu_usage(self, system_avg_cpu_usage: str) -> "QualityCpuUsageBuilder":
        self._quality_cpu_usage.system_avg_cpu_usage = system_avg_cpu_usage
        return self

    def system_max_cpu_usage(self, system_max_cpu_usage: str) -> "QualityCpuUsageBuilder":
        self._quality_cpu_usage.system_max_cpu_usage = system_max_cpu_usage
        return self

    def build(self) -> "QualityCpuUsage":
        return self._quality_cpu_usage
