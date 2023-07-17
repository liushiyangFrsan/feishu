# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchDeleteCollaboratorTaskResponseBody(object):
    _types = {
        "collaborators": List[str],
    }

    def __init__(self, d):
        self.collaborators: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteCollaboratorTaskResponseBodyBuilder":
        return BatchDeleteCollaboratorTaskResponseBodyBuilder()


class BatchDeleteCollaboratorTaskResponseBodyBuilder(object):
    def __init__(self,
                 batch_delete_collaborator_task_response_body: BatchDeleteCollaboratorTaskResponseBody = BatchDeleteCollaboratorTaskResponseBody(
                     {})) -> None:
        self._batch_delete_collaborator_task_response_body: BatchDeleteCollaboratorTaskResponseBody = batch_delete_collaborator_task_response_body

    def collaborators(self, collaborators: List[str]) -> "BatchDeleteCollaboratorTaskResponseBodyBuilder":
        self._batch_delete_collaborator_task_response_body.collaborators = collaborators
        return self

    def build(self) -> "BatchDeleteCollaboratorTaskResponseBody":
        return self._batch_delete_collaborator_task_response_body
