# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.wiki.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateSpaceMemberRequest = CreateSpaceMemberRequest.builder() \
        .space_id("1565676577122621") \
        .need_notification(True) \
        .request_body(Member.builder()
                      .member_type("str")
                      .member_id("str")
                      .member_role("str")
                      .build()) \
        .build()

    # 发起请求
    response: CreateSpaceMemberResponse = client.wiki.v2.space_member.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.wiki.v2.space_member.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
