import allure
from helpers.api_client import ApiClient

class TestLoginUser:
    @allure.title("Успешный вход под существующим пользователем")
    def test_login_existing_user_success(self, create_user_and_delete):
        user_data, _ = create_user_and_delete
        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = ApiClient.login_user(login_payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Ошибка входа с неверным логином и паролем")
    def test_login_invalid_credentials_error(self):
        login_payload = {
            "email": "invalid_user_test_999@test.com",
            "password": "wrongpassword123"
        }
        response = ApiClient.login_user(login_payload)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"