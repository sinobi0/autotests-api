import httpx
from tools.fakers import get_random_email
#Создаем нового пользователя
payload_create_user = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
create_user = httpx.post("http://localhost:8000/api/v1/users", json=payload_create_user)
assert create_user.status_code == 200, f"Некорректный статус-код ответа: {create_user.status_code}"
print(f"Пользовтель успшено создан, статус-код: {create_user.status_code}")

#Авторизуемся
payload_login = {
  "email": payload_create_user["email"],
  "password": payload_create_user["password"]
}
login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_login)
assert login.status_code == 200, f"Некорректный статус-код ответа {login.status_code}"
print(f"Аутентификация успешна, статус-код: {login.status_code}")
login_data = login.json()

#Меняем данные пользователя
headers_change_user = {"Authorization": f"Bearer {login_data['token']['accessToken']}"}
payload_change_user = {
    "email": get_random_email(),
    "password": payload_create_user["password"],
    "lastName": "Test",
    "firstName": "User",
    "middleName": "Name"
}
change_user = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user.json()['user']['id']}", json=payload_change_user, headers=headers_change_user)
assert change_user.status_code == 200, f"Некорректный статус-код: {change_user.status_code}"
print(f"Данные пользователя успешно изменены, статус-код: {change_user.status_code}")
