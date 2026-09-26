from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, GetCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_create_course_response(
        request: CreateCourseRequestSchema,
        response: CreateCourseResponseSchema
):
    """
    Verifies that create course response matches the request data.

    :param request: Initial create course request.
    :param response: API response with created course data.
    :raises AssertionError: If at least one field do not match.
    """
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.course.preview_file.id, request.preview_file_id,"preview_file_id")
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, "created_by_user_id")

def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Verifies that update course response matches the request data.

    :param request: Initial update course request.
    :param response: API response with updated course data.
    :raises AssertionError: If at least one field do not match.
    """
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

def assert_partial_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Verifies that update course response matches the request data

    :param request: Initial update course request.
    :param response: API response with updated course data.
    :raises AssertionError: If at least one field do not match.
    """
    if request.title is not None:
        assert_equal(response.course.title, request.title, "title")

    if request.max_score is not None:
        assert_equal(response.course.max_score, request.max_score, "max_score")

    if request.min_score is not None:
        assert_equal(response.course.min_score, request.min_score, "min_score")

    if request.description is not None:
        assert_equal(response.course.description, request.description, "description")

    if request.estimated_time is not None:
        assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")

def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Verifies that actual course data match the expected values.

    :param actual: Actual course data.
    :param expected: Expected course data.
    :raises AssertionError: If at least one value does not match.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Verifies that get courses response data matches the responses of each course creation.

    :param get_courses_response: API response to get courses.
    :param create_course_responses: List of API responses to create each course.
    :raises AssertionError: If data does not match.
    """
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)

def assert_get_course_response(
        get_course_response: GetCourseResponseSchema,
        course_response: CreateCourseResponseSchema | UpdateCourseResponseSchema
):
    """
    Verifies that course data in get course response equals data in create/update course response.

    :param get_course_response: API response to get course.
    :param course_response: Create/update course response data.
    :raises AssertionError: If responses do not match.
    """
    assert_course(actual=get_course_response.course, expected=course_response.course)
