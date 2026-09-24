from http import HTTPStatus

import pytest

from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_file_is_accessible, assert_get_file_response
from tools.assertions.schema import validate_json_schema
from fixtures.files import function_file, FileFixture


@pytest.mark.files
@pytest.mark.regression
class TestFiles:
    def test_create_file(self, files_client: FilesClient, function_file: FileFixture):
        request = CreateFileRequestSchema(upload_file="./testdata/files/Botticelli-primavera.jpg")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_file_response(request=request, response=response_data)
        assert_file_is_accessible(url=str(function_file.response.file.url))
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())
