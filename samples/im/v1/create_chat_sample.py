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
    request: CreateChatRequest = CreateChatRequest.builder() \
        .user_id_type("open_id") \
        .set_bot_manager(False) \
        .uuid("b13g2t38-1jd2-458b-8djf-dtbca5104204") \
        .request_body(CreateChatRequestBody.builder()
                      .avatar("default-avatar_44ae0ca3-e140-494b-956f-78091e348435")
                      .name("测试群名称")
                      .description("测试群描述")
                      .i18n_names(I18nNames.builder().build())
                      .owner_id("4d7a3c6g")
                      .user_id_list([])
                      .bot_id_list([])
                      .chat_mode("group")
                      .chat_type("private")
                      .external(False)
                      .join_message_visibility("all_members")
                      .leave_message_visibility("all_members")
                      .membership_approval("no_approval_required")
                      .restricted_mode_setting(RestrictedModeSetting.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: CreateChatResponse = client.im.v1.chat.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.chat.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
