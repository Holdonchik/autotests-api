from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from tools.fakers import fake


class FileSchema(BaseModel):
    """Describes the structure of create file."""
    id: str
    url: HttpUrl
    filename: str = Field(max_length=250)
    directory: str = Field(max_length=250)


class GetFileResponseSchema(BaseModel):
    """Describes the structure of get file response."""
    model_config = ConfigDict(extra="forbid")

    file: FileSchema


class CreateFileRequestSchema(BaseModel):
    """Describes the structure of create file request."""
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.jpg")
    directory: str = Field(default="tests")
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """Describes the structure of create file response"""
    model_config = ConfigDict(extra="forbid")

    file: FileSchema
