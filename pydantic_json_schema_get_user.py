from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

#Инициализируем публичный клиент
public_users_client = get_public_users_client()

#Создаем пользователя
create_users_request = CreateUserRequestSchema(
    email = get_random_email(),
    password = "password",
    last_name = "test",
    first_name = "test",
    middle_name = "test"
)
create_users_response = public_users_client.create_user(create_users_request)

#Инициализируем приватный клиент для авторизации
private_users_client = get_private_users_client(AuthenticationUserSchema(
    email = create_users_request.email,
    password = create_users_request.password
))
get_private_users_response = private_users_client.get_user_api(create_users_response.user.id)

#Проверяем на валидацию ответ на запрос get_user_api
get_private_users_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(get_private_users_response.json(), get_private_users_response_schema)