from httpx import Response

from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """ Client for interacting with the /api/v1/authentication endpoint."""

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Authenticates the user.

        :param request: A dictionary containing the user's email and password.
        :return: The server response as an httpx.Response object.
        """
        return self.post(
            url="/api/v1/authentication/login",
            json=request.model_dump(by_alias=True)
        )

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Refreshes the authentication token.

        :param request: A dictionary containing the refresh token.
        :return: The server response as an httpx.Response object.
        """
        return self.post(
            url="/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Logs in the user.

        :param request: A dictionary containing the login credentials.
        :return: Server response as a pydantic model.
        """
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Function creates an instance of AuthenticationClient with a preconfigured HTTP client.

    :return: Ready-to-use AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
