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
    request: SubmitApproveNotificationRequest = SubmitApproveNotificationRequest.builder() \
        .notification_id("6985032626234982420") \
        .request_body(SubmitApproveNotificationRequestBody.builder()
                      .reason("测试发送消息")
                      .build()) \
        .build()

    # 发起请求
    response: SubmitApproveNotificationResponse = client.helpdesk.v1.notification.submit_approve(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.notification.submit_approve failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
