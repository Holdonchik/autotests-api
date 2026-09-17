from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class Token(TypedDict):
    """Describes the structure of authentication token."""
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    """Describes the structure of authentication request."""
    email: str
    password: str


class LoginResponseDict(TypedDict):
    """Describes the structure of authentication response."""
    token: Token


class RefreshRequestDict(TypedDict):
    """ Describes the structure of the token refresh request."""
    refreshToken: str


class AuthenticationClient(APIClient):
    """ Client for interacting with the /api/v1/authentication endpoint."""

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Authenticates the user.

        :param request: A dictionary containing the user's email and password.
        :return: The server response as an httpx.Response object.
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Refreshes the authentication token.

        :param request: A dictionary containing the refresh token.
        :return: The server response as an httpx.Response object.
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Logs in the user.

        :param request: A dictionary containing the login credentials.
        :return: Server response as a dictionary.
        """
        response = self.login_api(request)
        return response.json()

def get_authentication_client() -> AuthenticationClient:
    """
    Function creates an instance of AuthenticationClient with a preconfigured HTTP client.

    :return: Ready-to-use AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
