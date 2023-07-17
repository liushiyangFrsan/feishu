# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .agent_schedule_update_info import AgentScheduleUpdateInfo


class PatchAgentSchedulesRequestBody(object):
    _types = {
        "agent_schedule": AgentScheduleUpdateInfo,
    }

    def __init__(self, d):
        self.agent_schedule: Optional[AgentScheduleUpdateInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchAgentSchedulesRequestBodyBuilder":
        return PatchAgentSchedulesRequestBodyBuilder()


class PatchAgentSchedulesRequestBodyBuilder(object):
    def __init__(self,
                 patch_agent_schedules_request_body: PatchAgentSchedulesRequestBody = PatchAgentSchedulesRequestBody(
                     {})) -> None:
        self._patch_agent_schedules_request_body: PatchAgentSchedulesRequestBody = patch_agent_schedules_request_body

    def agent_schedule(self, agent_schedule: AgentScheduleUpdateInfo) -> "PatchAgentSchedulesRequestBodyBuilder":
        self._patch_agent_schedules_request_body.agent_schedule = agent_schedule
        return self

    def build(self) -> "PatchAgentSchedulesRequestBody":
        return self._patch_agent_schedules_request_body
