import pytest
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema


class UserFixture(BaseModel):
    """Model for aggregating data returned by the `function_user` fixture """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

'''
NOTE: Структура именования {scope}_{сущность} позволяет легко управлять разными уровнями фикстур 
(function_user when scope="function", class_user when scope="class" etc).
NOTE2: Удаление данных после теста делает дебаг сложнее, поэтому в данном случае мы его избегаем.
'''
@pytest.fixture()
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)
