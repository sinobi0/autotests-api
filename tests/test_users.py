from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tests.conftest import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
def test_create_user(public_users_client: PublicUsersClient ):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(
        private_users_client: PrivateUsersClient,
        function_user: UserFixture
):

    get_users_me_response = private_users_client.get_user_me_api()
    get_users_me_response_data = GetUserResponseSchema.model_validate_json(get_users_me_response.text)
    assert_status_code(get_users_me_response.status_code, HTTPStatus.OK)
    assert_get_user_response(get_users_me_response_data.user, function_user.response.user)
    validate_json_schema(get_users_me_response.json(), get_users_me_response_data.model_json_schema())



