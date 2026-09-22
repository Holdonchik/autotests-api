from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Verifies that the response to create user request matches the request.

    :param request: Initial create user request data.
    :param response: API response with user data.
    :raises AssertionError: If at least one field does not match.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")
