import uuid

from pydantic import BaseModel, HttpUrl, Field


class FileSchema(BaseModel):
    """Describes the structure of create file."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    url: HttpUrl
    filename: str = Field(max_length=250)
    directory: str = Field(max_length=250)


class CreateFileRequestSchema(BaseModel):
    """Describes the structure of create file request."""
    filename: str
    filename: str = Field(max_length=250)
    directory: str = Field(max_length=250)


class CreateFileResponseSchema(BaseModel):
    """Describes the structure of create file response"""
    file: FileSchema
