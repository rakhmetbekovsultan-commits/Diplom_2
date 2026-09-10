import requests
import allure
from data.urls import LOGIN_USER_URL

class TestLoginUser:
    @allure.title("Успешный вход под существующим пользователем")
    def test_login_existing_user_success(self, create_user_and_delete):
        user_data, _ = create_user_and_delete
        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = requests.post(LOGIN_USER_URL, json=login_payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Ошибка входа с неверным логином и паролем")
    def test_login_invalid_credentials_error(self):
        login_payload = {
            "email": "invalid_user_test_999@test.com",
            "password": "wrongpassword123"
        }
        response = requests.post(LOGIN_USER_URL, json=login_payload)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"