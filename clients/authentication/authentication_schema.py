from pydantic import BaseModel, Field, EmailStr
from tools.fakers import fake


class TokenSchema(BaseModel):
    """Describes the structure of authentication token."""
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """Describes the structure of authentication request."""
    email: EmailStr = Field(default_factory=fake.email) # по умолчанию невалидный адрес
    password: str = Field(min_length=1, max_length=250, default_factory=fake.password) # по умолчанию невалидный пароль


class LoginResponseSchema(BaseModel):
    """Describes the structure of authentication response."""
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """ Describes the structure of the token refresh request."""
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence) # по умолчанию невалидный токен
