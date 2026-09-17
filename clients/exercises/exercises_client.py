from typing_extensions import TypedDict

from clients.api_client import APIClient

from httpx import Response


class GetExercisesQueryDict(TypedDict):
    """Describes the structure of get exercises query."""
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """Describes the structure of create exercise request."""
    title: str
    courseId: str
    maxScoreExpand: int | None
    minScoreExpand: int | None
    orderIndex: int | None
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict(TypedDict):
    """Describes the structure of update exercise request."""
    titleExpand: str | None
    maxScoreExpand: int | None
    minScoreExpand: int | None
    orderIndexExpand: int | None
    descriptionExpand: str | None
    estimatedTimeExpand: str | None


class ExercisesClient(APIClient):
    """Client for working with /api/v1/exercises."""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Method to get the list of exercises for specified course.

        :param query: Dictionary with courseId.
        :return: Server response as httpx.Response object.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api (self, exercise_id: str) -> Response:
        """
        Method to get information about specified exercise.

        :param exercise_id: Exercise identifier.
        :return: Server response as httpx.Response object.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self,  request: CreateExerciseRequestDict) -> Response:
        """
        Method to create exercise for specified course.

        :param request: Dictionary containing title, courseId, maxScoreExpand, minScoreExpand, orderIndex,
        description, estimatedTime
        :return: Server response as httpx.Response object.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Method to update exercise.

        :param exercise_id: Exercise identifier.
        :param request: Dictionary containing title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Server response as httpx.Response object.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to delete exercise.

        :param exercise_id: Exercise identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
