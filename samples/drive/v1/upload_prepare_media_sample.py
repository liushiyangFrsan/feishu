# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: UploadPrepareMediaRequest = UploadPrepareMediaRequest.builder() \
        .request_body(MediaUploadInfo.builder()
                      .file_name("123.txt")
                      .parent_type("doc_image")
                      .parent_node("fldcnxxxxxx")
                      .size(1024)
                      .extra("test")
                      .build()) \
        .build()

    # 发起请求
    response: UploadPrepareMediaResponse = client.drive.v1.media.upload_prepare(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.media.upload_prepare failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
