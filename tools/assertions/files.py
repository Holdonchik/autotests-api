from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, GetFileResponseSchema, \
    FileSchema
from tools.assertions.base import assert_equal
import httpx

from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


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

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that response to create file request with empty 'filename' value matches expected validation error.

    :param actual: API response with validation error to check.
    :raises AssertionError: If actual response does not match the expected.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that response to create file request with empty 'directory' value matches expected validation error.

    :param actual: API response with validation error to check.
    :raises AssertionError: If actual response does not match the expected.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    To verify error when file not found.

    :param actual: Actual response.
    :raises AssertionError: If actual response is not "File not found".
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)
