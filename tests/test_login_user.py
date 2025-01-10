import allure
import requests
from data import UserData
from urls import Urls

class TestLoginUser:

    @allure.title('Логин пользователя')
    @allure.description('Логин под существующим пользователем')
    def test_login_user(self):
        response = requests.post(Urls.LOGIN, data=UserData.data_correct)
        assert response.status_code == 200

    @allure.title('Логин пользователя')
    @allure.description('Логин с неверным логином и паролем')
    def test_login_user_with_incorrect_data(self):
        response = requests.post(Urls.LOGIN, data=UserData.data_incorrect)
        assert response.status_code == 401 and 'email or password are incorrect' in response.text