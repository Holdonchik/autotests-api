from typing import Any

from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Validates that JSON object (instance) complies to the specified JSON schema.

    :param instance: JSON data to validate.
    :param schema: Expected JSON schema.
    :raises jsonschema.exceptions.ValidationError: If the instance does not comply to the schema.
    """
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
