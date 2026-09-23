import pytest
from pydantic import BaseModel, EmailStr

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    """Model for aggregating user data for 'function_user' fixture."""
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)

# region Get client fixtures
@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(user=function_user.authentication_user)

# endregion

'''
NOTE: Структура именования {scope}_{сущность} позволяет легко управлять разными уровнями фикстур 
(function_user when scope="function", class_user when scope="class" etc).
NOTE2: Удаление данных после теста делает дебаг сложнее, поэтому в случае function_user мы его избегаем.
'''
@pytest.fixture()
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)
