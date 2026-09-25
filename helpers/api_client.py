import requests
import allure
from data.urls import CREATE_USER_URL, LOGIN_USER_URL, USER_URL, ORDERS_URL, INGREDIENTS_URL

class ApiClient:

    @staticmethod
    @allure.step("Создать пользователя: {user_data}")
    def register_user(user_data):
        return requests.post(CREATE_USER_URL, json=user_data)

    @staticmethod
    @allure.step("Авторизовать пользователя: {login_data}")
    def login_user(login_data):
        return requests.post(LOGIN_USER_URL, json=login_data)

    @staticmethod
    @allure.step("Удалить пользователя с токеном: {token}")
    def delete_user(token):
        return requests.delete(USER_URL, headers={"Authorization": token})

    @staticmethod
    @allure.step("Получить список ингредиентов")
    def get_ingredients():
        return requests.get(INGREDIENTS_URL)

    @staticmethod
    @allure.step("Создать заказ с токеном: {token}, данные: {payload}")
    def create_order(payload, token=None):
        headers = {"Authorization": token} if token else {}
        return requests.post(ORDERS_URL, headers=headers, json=payload)