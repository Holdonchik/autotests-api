from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class UpdateUserRequestDict(TypedDict):
    """Describes the structure of user update request."""
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


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

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Updates a user by ID.

        :param user_id: User identifier.
        :param request: Dictionary containing email, lastName, firstName, and middleName.
        :return: Server response as httpx.Response object.
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Deletes user by ID.

        :param user_id: User identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/users/{user_id}")

def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Function creates an instance of PrivateUsersClient with a preconfigured HTTP client.

    :return: Ready-to-use PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
