import pytest
from django.contrib.auth.models import User
from django.test import Client

from auth.utils.sign_in import SignInHandler


def test_sign_in_handler_init(client: Client):
    """
    Tests the initialization of the sign in handler
    and expects the attributes to be set correctly
    """

    sign_in_handler = SignInHandler(
        request=client,
        username="username",
        password="password",
    )

    assert sign_in_handler.request is not None
    assert sign_in_handler.username == "username"
    assert sign_in_handler.password == "password"
    assert sign_in_handler.errors == []
    assert sign_in_handler.user is None


@pytest.mark.parametrize(
    "username, password, errors, invalid",
    [
        ("", "", ["Username is required", "Password is required"], True),
        ("username", "", ["Password is required"], True),
        ("", "password", ["Username is required"], True),
        ("username", "password", [], False),
    ],
)
def test_sign_in_handler_validate_data(
    client: Client, username: str, password: str, errors: list[str], invalid: bool
):
    """
    Tests the validate_data method of the sign in handler
    and expects the errors and invalid attributes to be set correctly
    """

    sign_in_handler = SignInHandler(
        request=client,
        username=username,
        password=password,
    )

    sign_in_handler.validate_data()

    assert sign_in_handler.errors == errors
    assert sign_in_handler.invalid == invalid


@pytest.mark.django_db
def test_sign_in_handler_validate_user_invalid_credentials(client: Client):
    """
    Tests the validate_user method of the sign in handler
    and expects the user to be None and the errors to be set correctly
    """

    sign_in_handler = SignInHandler(
        request=client,
        username="username",
        password="password",
    )

    sign_in_handler.validate_user()

    assert sign_in_handler.user is None
    assert sign_in_handler.errors == ["Invalid credentials"]


@pytest.mark.django_db
def test_sign_in_handler_validate_user_valid_credentials(client: Client):
    """
    Tests the validate_user method of the sign in handler
    and expects the user to be set correctly and the errors to be empty
    """

    user = User.objects.create_user(username="username", password="password")

    sign_in_handler = SignInHandler(
        request=client,
        username="username",
        password="password",
    )

    sign_in_handler.validate_user()

    assert sign_in_handler.user == user
    assert sign_in_handler.errors == []
