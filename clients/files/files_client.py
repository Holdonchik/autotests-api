from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class FilesClient(APIClient):
    """Client for working with /api/v1/files."""

    def get_file_api(self, file_id: str) -> Response:
        """
        Get file method.

        :param file_id: File identifier.
        :return: Server response as httpx.Response object.
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Create file method.

        :param request: Pydantic model containing filename, directory, upload_file.
        :return: Server response as httpx.Response object.
        """
        return self.post(
            "/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": open(request.upload_file, 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Delete file method.

        :param file_id: File identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Create file method.

        :param request: Pydantic model  containing filename, directory, upload_file.
        :return: Pydantic model  containing file id, url, filename, directory.
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Function creates an instance of FilesClient with a preconfigured HTTP client.

    :return: Ready-to-use FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
