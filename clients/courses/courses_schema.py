import uuid

from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """Describes the structure of course."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(min_length=1, max_length=250)
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str = Field(min_length=1)
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCourseResponseSchema(BaseModel):
    """Describes the structure of get course response."""
    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """Describes the structure of get courses request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="userId")


class GetCoursesResponseSchema(BaseModel):
    """Describes the structure of get courses response."""
    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    """Describes the structure of create course request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str = Field(min_length=1, max_length=250)
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str = Field(min_length=1)
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="previewFileId")
    created_by_user_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """Describes the structure of create course response."""
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """Describes the structure of update course request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str | None = Field(min_length=1, max_length=250)
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime")

class UpdateCourseResponseSchema(BaseModel):
    """Describes the structure of update course response."""
    course: CourseSchema
