# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class TalentInterviewRegistration(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentInterviewRegistrationBuilder":
        return TalentInterviewRegistrationBuilder()


class TalentInterviewRegistrationBuilder(object):
    def __init__(self,
                 talent_interview_registration: TalentInterviewRegistration = TalentInterviewRegistration({})) -> None:
        self._talent_interview_registration: TalentInterviewRegistration = talent_interview_registration

    def build(self) -> "TalentInterviewRegistration":
        return self._talent_interview_registration
