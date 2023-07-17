# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.im.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: UpdateChatModerationRequest = UpdateChatModerationRequest.builder() \
        .chat_id("oc_a0553eda9014c201e6969b478895c230") \
        .user_id_type("user_id") \
        .request_body(UpdateChatModerationRequestBody.builder()
                      .moderation_setting("moderator_list")
                      .moderator_added_list([])
                      .moderator_removed_list([])
                      .build()) \
        .build()

    # 发起请求
    response: UpdateChatModerationResponse = client.im.v1.chat_moderation.update(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.chat_moderation.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
