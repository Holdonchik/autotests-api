from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, GetFileResponseSchema, \
    FileSchema
from tools.assertions.base import assert_equal
import httpx


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.
    Verifies that create files response matched the request/

    :param request: Initial request.
    :param response: API response with file data.
    :raises AssertionError: If at least one value does not match.
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

def assert_file_is_accessible(url: str):
    """
    Verifies that file is available at URL.

    :param url: File URL.
    :raises AssertionError: If file is not available.
    """
    response = httpx.get(url)
    assert response.status_code == 200, f"Файл недоступен по URL: {url}"

def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.
    Verifies that actual file data matched expected.

    :param actual: Actual file data.
    :param expected: Expected file data.
    :raises AssertionError: If at least one value does not match.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.
    Verifies that get file response data matches create file response data.

    :param get_file_response: API response to get file.
    :param create_file_response: API response to create file.
    :raises AssertionError: IF data does not match.
    """
    assert_file(get_file_response.file, create_file_response.file)
