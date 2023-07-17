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
    request: BindDepartmentUnitRequest = BindDepartmentUnitRequest.builder() \
        .request_body(BindDepartmentUnitRequestBody.builder()
                      .unit_id("BU121")
                      .department_id("od-4e6ac4d14bcd5071a37a39de902c7141")
                      .department_id_type("open_department_id")
                      .build()) \
        .build()

    # 发起请求
    response: BindDepartmentUnitResponse = client.contact.v3.unit.bind_department(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.unit.bind_department failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
