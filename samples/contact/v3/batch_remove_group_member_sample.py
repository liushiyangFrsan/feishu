# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.contact.v3 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: BatchRemoveGroupMemberRequest = BatchRemoveGroupMemberRequest.builder() \
        .group_id("test_group") \
        .request_body(BatchRemoveGroupMemberRequestBody.builder()
                      .members([])
                      .build()) \
        .build()

    # 发起请求
    response: BatchRemoveGroupMemberResponse = client.contact.v3.group_member.batch_remove(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.group_member.batch_remove failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
