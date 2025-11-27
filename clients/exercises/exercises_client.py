from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

class GetExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса создания упражнения
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str
    estimatedTime: str | None

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса удаления упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """
    def get_exercises_api(self, request: GetExercisesRequestDict) -> Response:
        """
        Метод получения списка упражнений
        :param request: словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения конкретного упражнения
        :param exercise_id: конкретный идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self,request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises",json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict ) -> Response:
        """
        Метод частичного обновления упражнения
        :param exercise_id: Идентификатор упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")