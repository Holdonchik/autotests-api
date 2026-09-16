import httpx


# Данные для входа в систему
login_payload = {
    "email": "test123@example.com",
    "password": "qwerty123"
}

# Запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
access_token = login_response.json()["token"]["accessToken"]

# Формируем заголовок с токеном
headers = {
    "Authorization" : f"Bearer {access_token}"
}

# Запрос данных о пользователе
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(user_response.status_code, user_response.json())
