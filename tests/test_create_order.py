import allure
import requests
from data import OrderData
from urls import Urls


class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('Создание заказа авторизованным пользователем с ингредиентами')
    def test_create_order_with_auth(self, create_user):
        token = create_user[1]
        headers = {'Authorization': token}
        response = requests.post(Urls.CREATE_ORDER, json=OrderData.data_for_correct_order, headers=headers)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Создание заказа')
    @allure.description('Создание заказа пользователем без авторизации с ингредиентами')
    def test_create_order_without_auth(self):
        response = requests.post(Urls.CREATE_ORDER,
                                 data=OrderData.data_for_correct_order)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.title('Создание заказа')
    @allure.description('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        response = requests.post(Urls.CREATE_ORDER)
        assert response.status_code == 400 and response.json()['message'] == "Ingredient ids must be provided"

    @allure.title('Создание заказа')
    @allure.description('Создание с невалидным хешем ингредиента')
    def test_create_order_with_invalid_ingredient_hash(self):
        response = requests.post(Urls.CREATE_ORDER, headers=Urls.headers,
                                 json=OrderData.data_for_incorrect_order)
        assert response.status_code == 500 and 'Internal Server Error' in response.text

