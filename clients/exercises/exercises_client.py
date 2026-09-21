from clients.api_client import APIClient

from httpx import Response

from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):
    """Client for working with /api/v1/exercises."""

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Method to get the list of exercises for specified course.

        :param query: Pydantic model with courseId.
        :return: Server response as httpx.Response object.
        """
        return self.get(
            url="/api/v1/exercises",
            params=query.model_dump(by_alias=True)
        )

    def get_exercise_api (self, exercise_id: str) -> Response:
        """
        Method to get information about specified exercise.

        :param exercise_id: Exercise identifier.
        :return: Server response as httpx.Response object.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self,  request: CreateExerciseRequestSchema) -> Response:
        """
        Method to create exercise for specified course.

        :param request: Pydantic model containing title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :return: Server response as httpx.Response object.
        """
        return self.post(
            url="/api/v1/exercises",
            json=request.model_dump(by_alias=True)
        )

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Method to update exercise.

        :param exercise_id: Exercise identifier.
        :param request: Pydantic model containing title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Server response as httpx.Response object.
        """
        return self.patch(
            url=f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True, exclude_none=True)
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to delete exercise.

        :param exercise_id: Exercise identifier.
        :return: Server response as httpx.Response object.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Gets information about specified exercise.

        :param exercise_id: Exercise identifier.
        :return: Pydantic model with exercise info: id, title, courseId, maxScore, minScore, orderIndex, description,
        estimatedTime
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def  get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Gets the list of exercises for specified course.

        :param query: Pydantic model with courseId.
        :return: Pydantic model with the list of exercises.
        """
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Creates exercise for specified course.

        :param request: Pydantic model containing title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime
        :return: Pydantic model with exercise info: id, title, courseId, maxScore, minScore, orderIndex, description,
        estimatedTime
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Updates exercise.

        :param exercise_id: Exercise identifier.
        :param request: Pydantic model containing title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Pydantic model with exercise info: id, title, courseId, maxScore, minScore, orderIndex, description,
        estimatedTime
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Function creates an instance of ExercisesClient with a preconfigured HTTP client.

    :return: Ready-to-use ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))
