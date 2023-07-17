# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.attendance.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateUserTaskRemedyRequest = CreateUserTaskRemedyRequest.builder() \
        .employee_type("employee_id") \
        .request_body(UserTaskRemedy.builder()
                      .user_id("abd754f7")
                      .remedy_date(20210701)
                      .punch_no(0)
                      .work_type(1)
                      .remedy_time("str")
                      .reason("忘记打卡")
                      .time("1611476284")
                      .build()) \
        .build()

    # 发起请求
    response: CreateUserTaskRemedyResponse = client.attendance.v1.user_task_remedy.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.attendance.v1.user_task_remedy.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
