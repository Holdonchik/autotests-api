from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
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

def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Verifies that user's id, email, last_name, first_name, middle_name have expected values.

    :param actual: Actual id, email, last_name, first_name, middle_name.
    :param expected: Expected id, email, last_name, first_name, middle_name.
    :raises AssertionError: If at least one value does not match.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

def assert_get_user_response( get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Verifies that user data in get user/get user me response equals data in create user response.

    :param get_user_response: Get user/get user me response data.
    :param create_user_response: Create user response data.
    :raises AssertionError: If responses do not match.
    """
    assert_user(actual=get_user_response.user, expected=create_user_response.user)
