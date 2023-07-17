# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class TenantAccessToken(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TenantAccessTokenBuilder":
        return TenantAccessTokenBuilder()


class TenantAccessTokenBuilder(object):
    def __init__(self, tenant_access_token: TenantAccessToken = TenantAccessToken({})) -> None:
        self._tenant_access_token: TenantAccessToken = tenant_access_token

    def build(self) -> "TenantAccessToken":
        return self._tenant_access_token
