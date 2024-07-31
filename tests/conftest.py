import pytest
from django.test import Client


@pytest.fixture
def client() -> Client:
    """
    Client fixture
    """

    return Client()
