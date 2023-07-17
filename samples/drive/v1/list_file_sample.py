# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListFileRequest = ListFileRequest.builder() \
        .page_size(10) \
        .page_token("MTY1NTA3MTA1OXw3MTA4NDc2MDc1NzkyOTI0Nabcef") \
        .folder_token("fldbcO1UuPz8VwnpPx5a9abcef") \
        .build()

    # 发起请求
    response: ListFileResponse = client.drive.v1.file.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.file.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
