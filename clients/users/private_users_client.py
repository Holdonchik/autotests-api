from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema

class PrivateUsersClient(APIClient):
    """Client for working with /api/v1/users."""

    def get_user_me_api(self) -> Response:
        """
        Retrieves current user.

        :return: Server response as httpx.Response object.
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Retrieves user by ID.

        :param user_id: User identifier.
        :return: Server response as httpx.Response object.
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Updates a user by ID.

        :param user_id: User identifier.
        :param request: Pydantic model containing email, lastName, firstName, and middleName.
        :return: Server response as httpx.Response object.
        """
        return self.patch(
            url=f"/api/v1/users/{user_id}",
            json=request.model_dump(by_alias=True)
        )

    def delete_user_api(self, user_id: str) -> Response:
        """
        Deletes user by ID.

        :param user_id: User identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Retrieves user by ID.

        :param user_id: User identifier.
        :return: Server response as a pydantic model.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Function creates an instance of PrivateUsersClient with a preconfigured HTTP client.

    :return: Ready-to-use PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
