import uuid

from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """Describes the structure of exercise."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(min_length=1, max_length=250)
    course_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str = Field(min_length=1)
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseResponseSchema(BaseModel):
    """Describes the structure of get exercises response."""
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """Describes the structure of get exercises query."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    course_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """Describes the structure of get exercises response."""
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """Describes the structure of create exercise request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str = Field(min_length=1, max_length=250)
    course_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str = Field(min_length=1)
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """Describes the structure of create exercise response."""
    exercise : ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """Describes the structure of update exercise request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str | None = Field(min_length=1, max_length=250)
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """Describes the structure of update exercise response."""
    exercise : ExerciseSchema
