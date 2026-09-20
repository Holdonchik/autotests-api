import uuid

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserSchema(BaseModel):
    """Describes the structure of user"""
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserRequestSchema(BaseModel):
    """Describes the structure of create user request."""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(max_length=250)
    password: str = Field(min_length=1, max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserResponseSchema(BaseModel):
    """Describes the structure of create user response."""
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """Describes the structure of get user response"""
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """Describes the structure of user update request."""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None = Field(max_length=250)
    last_name: str | None = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str | None = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str | None = Field(alias="middleName", min_length=1, max_length=50)


class UpdateUserResponseSchema(BaseModel):
    """Describes the structure of user update response."""
    user: UserSchema
