from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    """ Describes the structure of create user request."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """Client for interacting with  /api/v1/users public endpoint. """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Creates new user.

        :param request: Dictionary containing user's email, password, last name, first name and middle name.
        :return: The server response as httpx.Response object.
        """
        return self.post("/api/v1/users", json=request)

def get_public_users_client() -> PublicUsersClient:
    """
    Function creates an instance of PublicUsersClient with a preconfigured HTTP client.

    :return: Ready-to-use PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
