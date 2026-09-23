from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from fixtures.exercises import ExerciseFixture


def test_exercise(function_exercise: ExerciseFixture, exercises_client: ExercisesClient):
    request_data = CreateExerciseRequestSchema(course_id=function_exercise.request.course_id)
    create_exercise_response = exercises_client.create_exercise(request=request_data)
    print("Create exercise data:", create_exercise_response.exercise)
