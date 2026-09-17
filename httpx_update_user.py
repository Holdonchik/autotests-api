import httpx

from tools.fakers import get_random_email


# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "12345",
    "lastName": "Test",
    "firstName": "Testtest",
    "middleName": "Tst"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
print(create_user_response.status_code)
user_id = create_user_response.json()["user"]["id"]

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
print(login_response.status_code)
access_token = login_response.json()["token"]["accessToken"]

# Редактируем пользователя
update_user_headers = {
    "Authorization" : f"Bearer {access_token}"
}
update_user_payload = {
    "email": get_random_email(),
    "password": "qwerty",
    "lastName": "Doe",
    "firstName": "John",
    "middleName": "Junior"
}
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{user_id}", headers=update_user_headers, json=update_user_payload
)
print(update_user_response.status_code, update_user_response.json())
