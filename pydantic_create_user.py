import uuid
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Describes the structure of user."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserRequestSchema(BaseModel):
    """Describes the structure of create user request."""
    email: EmailStr
    password: str = Field(min_length=1, max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserResponseSchema(BaseModel):
    """Describes the structure of create user response."""
    user: UserSchema
