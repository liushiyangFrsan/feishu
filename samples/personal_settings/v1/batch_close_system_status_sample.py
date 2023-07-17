# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.personal_settings.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: BatchCloseSystemStatusRequest = BatchCloseSystemStatusRequest.builder() \
        .system_status_id("7101214603622940671") \
        .user_id_type("open_id") \
        .request_body(BatchCloseSystemStatusRequestBody.builder()
                      .user_list([])
                      .build()) \
        .build()

    # 发起请求
    response: BatchCloseSystemStatusResponse = client.personal_settings.v1.system_status.batch_close(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.personal_settings.v1.system_status.batch_close failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
