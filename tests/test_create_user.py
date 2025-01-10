import pytest
import allure
import requests
from data import UserData
from urls import Urls

class TestCreateUser:

    @allure.title('Создание пользователя')
    @allure.description('Создание уникального пользователя')
    def test_create_new_user_is_correct(self):
        response = requests.post(Urls.CREATE_USER, data=UserData.create_random_user())
        assert response.status_code == 200

    @allure.title('Создание пользователя')
    @allure.description('Создание пользователя, который уже зарегистрирован')
    def test_impossible_recreate_user(self):
        response = requests.post(Urls.CREATE_USER, data=UserData.data_double)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('Создание пользователя')
    @allure.description('Создание пользователя с одним незаполненным обязательным полем')
    @pytest.mark.parametrize("user_data", [UserData.data_with_empty_email,
                                           UserData.data_with_empty_password,
                                           UserData.data_with_empty_name])
    def test_create_user_with_empty_fields(self, user_data):
        response = requests.post(Urls.CREATE_USER, data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text