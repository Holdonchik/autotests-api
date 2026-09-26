from collections.abc import Callable
from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCourseResponseSchema, GetCoursesQuerySchema, GetCoursesResponseSchema, CreateCourseResponseSchema, \
    CreateCourseRequestSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_partial_update_course_response, \
    assert_get_course_response, assert_get_courses_response, assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        update_request = UpdateCourseRequestSchema()
        update_response = courses_client.update_course_api(function_course.response.course.id, update_request)
        update_response_data = UpdateCourseResponseSchema.model_validate_json(update_response.text)
        assert_status_code(update_response.status_code, HTTPStatus.OK)
        assert_update_course_response(update_request, update_response_data)
        validate_json_schema(update_response.json(), update_response_data.model_json_schema())
        # Доп проверка
        get_response = courses_client.get_course_api(course_id=function_course.response.course.id)
        get_response_data = GetCourseResponseSchema.model_validate_json(get_response.text)
        assert_get_course_response(get_response_data, update_response_data)

    def test_partial_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        update_request = UpdateCourseRequestSchema(title=None, min_score=None, max_score=None)
        update_response = courses_client.update_course_api(function_course.response.course.id, update_request)
        update_response_data = UpdateCourseResponseSchema.model_validate_json(update_response.text)
        assert_status_code(update_response.status_code, HTTPStatus.OK)
        assert_partial_update_course_response(update_request, update_response_data)
        validate_json_schema(update_response.json(), update_response_data.model_json_schema())
        # Доп проверка
        get_response = courses_client.get_course_api(course_id=function_course.response.course.id)
        get_response_data = GetCourseResponseSchema.model_validate_json(get_response.text)
        assert_get_course_response(get_response_data, update_response_data)

    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_course: CourseFixture
    ):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_courses_multiple(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_courses_factory: Callable
    ):
        courses = function_courses_factory(5)
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_get_courses_response(response_data, courses)

    def test_create_course(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_file: FileFixture
            ):
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id
        )
        response = courses_client.create_course_api(request=request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request=request, response=response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

        # Доп проверка с get
        get_response = courses_client.get_course_api(course_id=response_data.course.id)
        get_response_data = GetCourseResponseSchema.model_validate_json(get_response.text)
        assert_get_course_response(get_response_data, response_data)
