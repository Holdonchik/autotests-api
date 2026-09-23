from clients.courses.courses_client import  CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema
from fixtures.courses import CourseFixture


def test_course(function_course: CourseFixture, courses_client: CoursesClient):
    request_data = CreateCourseRequestSchema(
        preview_file_id=function_course.request.preview_file_id,
        created_by_user_id=function_course.request.created_by_user_id
    )
    create_course_response = courses_client.create_course(request_data)
    print("Create course data:", create_course_response.course)
