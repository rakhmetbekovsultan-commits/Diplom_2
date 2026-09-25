import allure
from helpers.api_client import ApiClient

class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_and_ingredients_success(self, create_user_and_delete):
        _, user_response = create_user_and_delete
        token = user_response.json()["accessToken"]

        ingredients_response = ApiClient.get_ingredients()
        ingredient_id = ingredients_response.json()["data"][0]["_id"]

        payload = {"ingredients": [ingredient_id]}
        response = ApiClient.create_order(payload, token=token)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth_success(self):
        ingredients_response = ApiClient.get_ingredients()
        ingredient_id = ingredients_response.json()["data"][0]["_id"]

        payload = {"ingredients": [ingredient_id]}
        response = ApiClient.create_order(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Ошибка при создании заказа без ингредиентов")
    def test_create_order_without_ingredients_error(self):
        payload = {"ingredients": []}
        response = ApiClient.create_order(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Ошибка при создании заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredient_hash_error(self):
        payload = {"ingredients": ["invalid_hash_123456789"]}
        response = ApiClient.create_order(payload)

        assert response.status_code == 500