from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Verifies that actual response status code matches the expected one.

    :param actual: Actual response status code.
    :param expected: Expected response status code.
    :raises AssertionError: If status codes do not match.
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Verifies that actual value equals to expected value.

    :param name: The name of the value being verified.
    :param actual: Actual value.
    :param expected: Expected value.
    :raises AssertionError: If actual value is not equal to expected value.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )

def assert_is_true(actual: Any, name: str):
    """
    Verifies that actual value evaluates to True.

    :param name: Name of the value being verified.
    :param actual: Actual value.
    :raises AssertionError: If actual value evaluates to False.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )
