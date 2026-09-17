from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateFileRequestDict(TypedDict):
    """Describes the structure of create file request."""
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """Client for working with /api/v1/files."""

    def get_file_api(self, file_id: str) -> Response:
        """
        Get file method.

        :param file_id: File identifier.
        :return: Server response as httpx.Response object.
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Create file method.

        :param request: Dictionary containing filename, directory, upload_file.
        :return: Server response as httpx.Response object.
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Delete file method.

        :param file_id: File identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/files/{file_id}")
