from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """Describes the structure of exercise."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str
    title: str = Field(min_length=1, max_length=250)
    course_id: str = Field(alias="courseId")
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

    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """Describes the structure of get exercises response."""
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """Describes the structure of create exercise request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str = Field(min_length=1, max_length=250, default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4) # по умолчанию невалидный id
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(min_length=1, default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CreateExerciseResponseSchema(BaseModel):
    """Describes the structure of create exercise response."""
    exercise : ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """Describes the structure of update exercise request."""
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str | None = Field(min_length=1, max_length=250, default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(min_length=1, default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    """Describes the structure of update exercise response."""
    exercise : ExerciseSchema
