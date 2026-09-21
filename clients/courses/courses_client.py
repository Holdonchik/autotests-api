from httpx import Response
from clients.api_client import APIClient
from clients.courses.courses_schema import (
    GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, CreateCourseResponseSchema,
    UpdateCourseResponseSchema, GetCourseResponseSchema, GetCoursesResponseSchema
)

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class CoursesClient(APIClient):
    """Client for working with /api/v1/courses."""

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Method to get the list of courses.

        :param query: Pydantic model with userId.
        :return: Server response as httpx.Response object.
        """
        return self.get(
            url="/api/v1/courses",
            params=query.model_dump(by_alias=True)
        )

    def get_course_api(self, course_id: str) -> Response:
        """
        Method to get course.

        :param course_id: Course identifier.
        :return: Server response as httpx.Response object.
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Method to create course.

        :param request: Pydantic model containing title, maxScore, minScore, description, estimatedTime,
         previewFileId, createdByUserId.
        :return: Server response as httpx.Response object.
        """
        return self.post(
            url="/api/v1/courses",
            json=request.model_dump(by_alias=True)
        )

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Method to update course.

        :param course_id: Course identifier.
        :param request: Pydantic model containing title, maxScore, minScore, description, estimatedTime.
        :return: Server response as httpx.Response object.
        """
        return self.patch(
            url=f"/api/v1/courses/{course_id}",
            json=request.model_dump(by_alias=True, exclude_none=True)
        )

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method to delete course.

        :param course_id: Course identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Creates course.

        :param request: Pydantic model containing title, maxScore, minScore, description, estimatedTime,
         previewFileId, createdByUserId.
        :return: Pydantic model with course info: id, title, maxScore, minScore, description, previewFileId,
        estimatedTime, createdByUser
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def update_course(self, request: UpdateCourseRequestSchema, course_id: str) -> UpdateCourseResponseSchema:
        """
        Updates course.

        :param course_id: Course identifier.
        :param request: Pydantic model containing title, maxScore, minScore, description, estimatedTime,
         previewFileId, createdByUserId.
        :return: Pydantic model with course info: id, title, maxScore, minScore, description, previewFileId,
        estimatedTime, createdByUser
        """
        response = self.update_course_api(
            request=request,
            course_id=course_id
        )
        return UpdateCourseResponseSchema.model_validate_json(response.text)

    def get_course(self, course_id: str) -> GetCourseResponseSchema:
        """
        Gets course.

        :param course_id: Course identifier.
        :return: Pydantic model with course info: id, title, maxScore, minScore, description, previewFileId,
        estimatedTime, createdByUser
        """
        response = self.get_course_api(course_id=course_id)
        return GetCourseResponseSchema.model_validate_json(response.text)

    def get_courses(self, query: GetCoursesQuerySchema) -> GetCoursesResponseSchema:
        """
        Gets courses for specified user.

        :param query: Pydantic model with userId.
        :return: List of courses.
        """
        response = self.get_courses_api(query=query)
        return GetCoursesResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Function creates an instance of CoursesClient with a preconfigured HTTP client.

    :return: Ready-to-use CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
