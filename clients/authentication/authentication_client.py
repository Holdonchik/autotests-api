from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """ Describes the structure of the authentication request. """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """ Describes the structure of the token refresh request. """
    refreshToken: str


class AuthenticationClient(APIClient):
    """ Client for interacting with the /api/v1/authentication endpoint. """

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
