# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.application.v6 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchApplicationFeedbackRequest = PatchApplicationFeedbackRequest.builder() \
        .app_id("cli_9f115af860f7901b") \
        .feedback_id("7057888018203574291") \
        .user_id_type("open_id") \
        .status(1) \
        .operator_id("ou_9565b69967831233761cc2f11b4c089f") \
        .build()

    # 发起请求
    response: PatchApplicationFeedbackResponse = client.application.v6.application_feedback.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.application_feedback.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
