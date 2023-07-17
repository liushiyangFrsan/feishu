# Code generated by Lark OpenAPI.

from typing import *
from typing import IO

from lark_oapi.core.construct import init


class UploadImageRequestBody(object):
    _types = {
        "data": IO[Any],
        "target_id": int,
        "target_type": int,
    }

    def __init__(self, d):
        self.data: Optional[IO[Any]] = None
        self.target_id: Optional[int] = None
        self.target_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadImageRequestBodyBuilder":
        return UploadImageRequestBodyBuilder()


class UploadImageRequestBodyBuilder(object):
    def __init__(self, upload_image_request_body: UploadImageRequestBody = UploadImageRequestBody({})) -> None:
        self._upload_image_request_body: UploadImageRequestBody = upload_image_request_body

    def data(self, data: IO[Any]) -> "UploadImageRequestBodyBuilder":
        self._upload_image_request_body.data = data
        return self

    def target_id(self, target_id: int) -> "UploadImageRequestBodyBuilder":
        self._upload_image_request_body.target_id = target_id
        return self

    def target_type(self, target_type: int) -> "UploadImageRequestBodyBuilder":
        self._upload_image_request_body.target_type = target_type
        return self

    def build(self) -> "UploadImageRequestBody":
        return self._upload_image_request_body
