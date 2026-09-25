import pytest
from helpers.api_client import ApiClient
from helpers.user_generator import generate_user_data

@pytest.fixture
def create_user_and_delete():
    user_data = generate_user_data()
    response = ApiClient.register_user(user_data)
    token = response.json().get("accessToken")

    yield user_data, response

    if token:
        ApiClient.delete_user(token)