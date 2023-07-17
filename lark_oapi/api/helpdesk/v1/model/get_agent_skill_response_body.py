# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .agent_skill import AgentSkill


class GetAgentSkillResponseBody(object):
    _types = {
        "agent_skill": AgentSkill,
    }

    def __init__(self, d):
        self.agent_skill: Optional[AgentSkill] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAgentSkillResponseBodyBuilder":
        return GetAgentSkillResponseBodyBuilder()


class GetAgentSkillResponseBodyBuilder(object):
    def __init__(self,
                 get_agent_skill_response_body: GetAgentSkillResponseBody = GetAgentSkillResponseBody({})) -> None:
        self._get_agent_skill_response_body: GetAgentSkillResponseBody = get_agent_skill_response_body

    def agent_skill(self, agent_skill: AgentSkill) -> "GetAgentSkillResponseBodyBuilder":
        self._get_agent_skill_response_body.agent_skill = agent_skill
        return self

    def build(self) -> "GetAgentSkillResponseBody":
        return self._get_agent_skill_response_body
