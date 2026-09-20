from typing_extensions import TypedDict

from clients.api_client import APIClient

from httpx import Response

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class Exercise(TypedDict):
    """Describes the structure of exercise."""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseResponseDict(TypedDict):
    """Describes the structure of get exercises response."""
    exercise: Exercise


class GetExercisesQueryDict(TypedDict):
    """Describes the structure of get exercises query."""
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """Describes the structure of get exercises response."""
    exercises: list[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """Describes the structure of create exercise request."""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """Describes the structure of create exercise response."""
    exercise : Exercise


class UpdateExerciseRequestDict(TypedDict):
    """Describes the structure of update exercise request."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """Describes the structure of update exercise response."""
    exercise : Exercise


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

        :param request: Dictionary containing title, courseId, maxScore, minScore, orderIndex,
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

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Gets information about specified exercise.

        :param exercise_id: Exercise identifier.
        :return: Dictionary with exercise info: id, title, courseId, maxScore, minScore, orderIndex, description,
        estimatedTime
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def  get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Gets the list of exercises for specified course.

        :param query: Dictionary with courseId.
        :return: Dictionary with the list of exercises.
        """
        response = self.get_exercises_api(self, query=query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Creates exercise for specified course.

        :param request: Dictionary containing title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :return: Dictionary with exercise info: id, title, courseId, maxScore, minScore, orderIndex, description,
        estimatedTime
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Updates exercise.

        :param exercise_id: Exercise identifier.
        :param request: Dictionary containing title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Dictionary with exercise info: id, title, courseId, maxScore, minScore, orderIndex, description,
        estimatedTime
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Function creates an instance of ExercisesClient with a preconfigured HTTP client.

    :return: Ready-to-use ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))
