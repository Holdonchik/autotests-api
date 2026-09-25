from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCourseResponseSchema
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_partial_update_course_response, \
    assert_get_course_response
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
