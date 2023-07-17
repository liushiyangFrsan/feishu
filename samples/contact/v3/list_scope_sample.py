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
    request: ListScopeRequest = ListScopeRequest.builder() \
        .user_id_type("open_id") \
        .department_id_type("open_department_id") \
        .page_token(
        "AQD9/Rn9eij9Pm39ED40/dk53s4Ebp882DYfFaPFbz00L4CMZJrqGdzNyc8BcZtDbwVUvRmQTvyMYicnGWrde9X56TgdBuS+JKiSIkdexPw=") \
        .page_size(50) \
        .build()

    # 发起请求
    response: ListScopeResponse = client.contact.v3.scope.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.scope.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
