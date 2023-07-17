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
    request: PatchNotificationRequest = PatchNotificationRequest.builder() \
        .notification_id("6985032626234982420") \
        .user_id_type("user_id") \
        .request_body(Notification.builder()
                      .id("6981801914270744596")
                      .job_name("测试推送任务")
                      .status(0)
                      .create_user(NotificationUser.builder().build())
                      .created_at("1626332244719")
                      .update_user(NotificationUser.builder().build())
                      .updated_at("1626332244719")
                      .target_user_count(1)
                      .sent_user_count(1)
                      .read_user_count(1)
                      .send_at("1626332244719")
                      .push_content("")
                      .push_type(0)
                      .push_scope_type(0)
                      .new_staff_scope_type(0)
                      .new_staff_scope_department_list([])
                      .user_list([])
                      .department_list([])
                      .chat_list([])
                      .ext("{}")
                      .build()) \
        .build()

    # 发起请求
    response: PatchNotificationResponse = client.helpdesk.v1.notification.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.notification.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
