# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    file = open("file_path", "rb")
    request: UploadPersonRequest = UploadPersonRequest.builder() \
        .request_body(UploadPersonRequestBody.builder()
                      .file_content(file)
                      .file_name("个人信息")
                      .build()) \
        .build()

    # 发起请求
    response: UploadPersonResponse = client.corehr.v1.person.upload(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.person.upload failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
