# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.helpdesk.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PreviewNotificationRequest = PreviewNotificationRequest.builder() \
        .notification_id("6985032626234982420") \
        .build()

    # 发起请求
    response: PreviewNotificationResponse = client.helpdesk.v1.notification.preview(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.notification.preview failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
