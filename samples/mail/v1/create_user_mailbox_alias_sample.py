# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.mail.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateUserMailboxAliasRequest = CreateUserMailboxAliasRequest.builder() \
        .user_mailbox_id("user@xxx.xx") \
        .request_body(EmailAlias.builder()
                      .email_alias("email_alias@xxx.xx")
                      .build()) \
        .build()

    # 发起请求
    response: CreateUserMailboxAliasResponse = client.mail.v1.user_mailbox_alias.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.mail.v1.user_mailbox_alias.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
