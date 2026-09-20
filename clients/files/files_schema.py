import uuid

from pydantic import BaseModel, HttpUrl, Field


class FileSchema(BaseModel):
    """Describes the structure of create file."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """Describes the structure of create file request."""
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """Describes the structure of create file response"""
    file: FileSchema
