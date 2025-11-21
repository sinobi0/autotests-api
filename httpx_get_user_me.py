import httpx
#Тело запроса к эндпоинту /authentication/login
login_payload = {
    "email": "user@example.com",
    "password": "string"
}
#Пытаемся отправить запрос
try:
    login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
    login_response.raise_for_status()
#Отлавливаем некорректный статус код
except httpx.HTTPStatusError as e:
    print("Ошибка запроса:", e)
login_data = login_response.json()
access_token = login_data["token"]["accessToken"]

#Заголовки для запроса /users/me
headers_users = {
    "Authorization": f"Bearer {access_token}"
}
#Пытаемся отправить запрос
try:
    user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_users)
    user_response.raise_for_status()
#Отлавливаем некорректный статус код
except httpx.HTTPStatusError as e:
    print("Ошибка запроса:", e)
user_data = user_response.json()
print(f"Данные пользователя: {user_data}")
print(f"Статус код: {user_response.status_code}")