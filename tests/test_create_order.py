import requests
import allure
from data.urls import ORDERS_URL, INGREDIENTS_URL

class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_and_ingredients_success(self, create_user_and_delete):
        _, user_response = create_user_and_delete
        token = user_response.json()["accessToken"]

        ingredients_response = requests.get(INGREDIENTS_URL)
        ingredient_id = ingredients_response.json()["data"][0]["_id"]

        headers = {"Authorization": token}
        payload = {"ingredients": [ingredient_id]}

        response = requests.post(ORDERS_URL, headers=headers, json=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth_success(self):
        ingredients_response = requests.get(INGREDIENTS_URL)
        ingredient_id = ingredients_response.json()["data"][0]["_id"]

        payload = {"ingredients": [ingredient_id]}
        response = requests.post(ORDERS_URL, json=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Ошибка при создании заказа без ингредиентов")
    def test_create_order_without_ingredients_error(self):
        payload = {"ingredients": []}
        response = requests.post(ORDERS_URL, json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Ошибка при создании заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredient_hash_error(self):
        payload = {"ingredients": ["invalid_hash_123456789"]}
        response = requests.post(ORDERS_URL, json=payload)
        assert response.status_code == 500