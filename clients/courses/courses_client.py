from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import FileSchema

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.users_schema import UserSchema


class Course(TypedDict):
    """Describes the structure of course."""
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema


class GetCoursesQueryDict(TypedDict):
    """Describes the structure of get courses request."""
    userId: str


class CreateCourseRequestDict(TypedDict):
    """Describes the structure of create course request."""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseDict(TypedDict):
    """Describes the structure of create course response."""
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """Describes the structure of update course request."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """Client for working with /api/v1/courses."""

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Method to get the list of courses.

        :param query: Dictionary with userId.
        :return: Server response as httpx.Response object.
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Method to get course.

        :param course_id: Course identifier.
        :return: Server response as httpx.Response object.
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Method to create course.

        :param request: Dictionary containing title, maxScore, minScore, description, estimatedTime,
         previewFileId, createdByUserId.
        :return: Server response as httpx.Response object.
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Method to update course.

        :param course_id: Course identifier.
        :param request: Dictionary containing title, maxScore, minScore, description, estimatedTime.
        :return: Server response as httpx.Response object.
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method to delete course.

        :param course_id: Course identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        """
        Creates course.

        :param request: Dictionary containing title, maxScore, minScore, description, estimatedTime,
         previewFileId, createdByUserId.
        :return: Dictionary with course info: id, title, maxScore, minScore, description, previewFileId, estimatedTime,
        createdByUser
        """
        response = self.create_course_api(request)
        return response.json()

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Function creates an instance of CoursesClient with a preconfigured HTTP client.

    :return: Ready-to-use CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
