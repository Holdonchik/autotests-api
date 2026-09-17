from typing import Any

from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles


class APIClient:
    """ Base client for making HTTP requests. """
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Executes a GET request.

        :param url: The endpoint URL.
        :param params: GET request parameters (e.g., ?key=value).
        :return: A Response object containing the response data.
        """
        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Executes a POST request.

        :param url: The endpoint URL.
        :param json: Data in JSON format.
        :param data: Form-encoded data (e.g., application/x-www-form-urlencoded).
        :param files: Files to upload to the server.
        :return: A Response object containing the response data.
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Executes a PATCH request (partial update of data).

        :param url: The endpoint URL.
        :param json: Data to update in JSON format.
        :return: A Response object containing the response data.
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Executes a DELETE request (deletion of data).

        :param url: The endpoint URL.
        :return: A Response object containing the response data.
        """
        return self.client.delete(url)
