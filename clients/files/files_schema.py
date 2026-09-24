from pydantic import BaseModel, HttpUrl, Field, ConfigDict, UUID4
from tools.fakers import fake


class FileSchema(BaseModel):
    """Describes the structure of create file."""
    id: UUID4
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

class CreateFileInvalidRequestSchema(BaseModel):
    """Describes the structure to form incorrect create file request."""
    filename: str | None = Field(default_factory=lambda: f"{fake.uuid4()}.jpg")
    directory: str | None = Field(default="tests")
    upload_file: str | None
