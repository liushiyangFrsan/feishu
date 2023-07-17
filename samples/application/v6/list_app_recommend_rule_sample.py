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
    request: ListAppRecommendRuleRequest = ListAppRecommendRuleRequest.builder() \
        .page_size(10) \
        .page_token("new-e11ee058b4a8ed2881da11ac7e37c4fc") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: ListAppRecommendRuleResponse = client.application.v6.app_recommend_rule.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.app_recommend_rule.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
