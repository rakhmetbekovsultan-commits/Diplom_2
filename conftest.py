import pytest
import requests
from data.urls import CREATE_USER_URL, USER_URL
from helpers.user_generator import generate_user_data

@pytest.fixture
def create_user_and_delete():
    user_data = generate_user_data()
    response = requests.post(CREATE_USER_URL, json=user_data)
    token = response.json().get("accessToken")

    yield user_data, response

    if token:
        requests.delete(USER_URL, headers={"Authorization": token})