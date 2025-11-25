from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

class UsersClientRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: UsersClientRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.
        :param request: Словарь с необходимыми данными для создания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.post("/api/v1/users", json = request)
