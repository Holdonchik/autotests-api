from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """Describes the structure of course."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str
    title: str = Field(min_length=1, max_length=250)
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str = Field(min_length=1)
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCourseResponseSchema(BaseModel):
    """Describes the structure of get course response."""
    model_config = ConfigDict(extra="forbid")

    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """Describes the structure of get courses request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    user_id: str = Field(alias="userId")


class GetCoursesResponseSchema(BaseModel):
    """Describes the structure of get courses response."""
    model_config = ConfigDict(extra="forbid")

    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    """Describes the structure of create course request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4) # по умолчанию невалидный id
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4) # по умолчанию невалидный id


class CreateCourseResponseSchema(BaseModel):
    """Describes the structure of create course response."""
    model_config = ConfigDict(extra="forbid")

    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """Describes the structure of update course request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateCourseResponseSchema(BaseModel):
    """Describes the structure of update course response."""
    model_config = ConfigDict(extra="forbid")

    course: CourseSchema
