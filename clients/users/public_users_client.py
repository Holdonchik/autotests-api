from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """Client for interacting with  /api/v1/users public endpoint. """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Creates new user.

        :param request: Pydantic model containing user's email, password, last name, first name and middle name.
        :return: The server response as httpx.Response object.
        """
        return self.post(
            url="/api/v1/users",
            json=request.model_dump(by_alias=True)
        )

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Creates new user.

        :param request: Pydantic model containing user's id, email, last name, first name and middle name.
        :return: Server response as a pydantic model.
        """
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Function creates an instance of PublicUsersClient with a preconfigured HTTP client.

    :return: Ready-to-use PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
