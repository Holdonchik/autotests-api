from pydantic import BaseModel, EmailStr, Field, ConfigDict, UUID4

from tools.fakers import fake


class UserSchema(BaseModel):
    """Describes the structure of user"""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: UUID4
    email: EmailStr = Field(max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserRequestSchema(BaseModel):
    """Describes the structure of create user request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """Describes the structure of create user response."""
    model_config = ConfigDict(extra="forbid")

    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """Describes the structure of get user response"""
    model_config = ConfigDict(extra="forbid")

    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """Describes the structure of user update request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.first_name)


class UpdateUserResponseSchema(BaseModel):
    """Describes the structure of user update response."""
    model_config = ConfigDict(extra="forbid")

    user: UserSchema
