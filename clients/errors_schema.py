from typing import Any

from pydantic import BaseModel, Field, ConfigDict


class ValidationErrorSchema(BaseModel):
    """Describes the structure of API validation error."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseSchema(BaseModel):
    """Describes the structure of API response containing validation error."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BaseModel):
    """Describes the structure of internal error."""

    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias="detail")
