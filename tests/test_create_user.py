import pytest
import requests
import allure
from data.urls import CREATE_USER_URL
from helpers.user_generator import generate_user_data

class TestCreateUser:
    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self, create_user_and_delete):
        _, response = create_user_and_delete
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Ошибка при создании уже зарегистрированного пользователя")
    def test_create_existing_user_error(self, create_user_and_delete):
        user_data, _ = create_user_and_delete
        response = requests.post(CREATE_USER_URL, json=user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Ошибка при создании пользователя без заполнения обязательного поля")
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_missing_field_error(self, field):
        user_data = generate_user_data()
        user_data.pop(field)
        response = requests.post(CREATE_USER_URL, json=user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"