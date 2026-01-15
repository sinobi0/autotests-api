import pytest
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from fixtures.courses import CourseFixture
from fixtures.users import function_user, UserFixture
from pydantic import BaseModel
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema

class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
        function_course: CourseFixture,
        exercises_client: ExercisesClient,
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(
        course_id = function_course.response.course.id
    )
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)

