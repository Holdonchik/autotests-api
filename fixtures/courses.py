from collections.abc import Callable

import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    """Model for aggregating course data for 'function_course' fixture."""
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(user=function_user.authentication_user)

@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request=request)
    return CourseFixture(request=request, response=response)

@pytest.fixture
def function_courses_factory(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> Callable[[int], list[CreateCourseResponseSchema]]:
    def _function_courses_factory(required_courses_count: int) -> list[CreateCourseResponseSchema]:
        responses = []
        for _ in range(required_courses_count):
            request = CreateCourseRequestSchema(
                preview_file_id=function_file.response.file.id,
                created_by_user_id=function_user.response.user.id
            )
            response = courses_client.create_course(request=request)
            responses.append(response)
        return responses
    return _function_courses_factory
