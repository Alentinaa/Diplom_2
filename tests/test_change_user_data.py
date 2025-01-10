import pytest
import allure
import requests
from data import UserData
from urls import Urls

class TestChangeUserData:

    @pytest.mark.parametrize(
        "payload_data, field_name",
        [
            ({"email": UserData.create_random_user()["email"]}, "email"),
            ({"password": UserData.create_random_user()["password"]}, "password"),
            ({"name": UserData.create_random_user()["name"]}, "name")
        ]
    )
    @allure.title("Изменение данных уже авторизованного пользователя")
    @allure.description("При попытке изменить email/password/name авторизованного пользователя, изменение данных происходит успешно")
    def test_change_authorized_user_data(self, create_user, payload_data, field_name):
            token = {'Authorization': create_user[1]}
            r = requests.patch(Urls.CHANGE_USER_DATA, headers=token, json=payload_data)
            assert r.status_code == 200

    @allure.title("Изменение данных пользователя с авторизацией")
    @allure.description("Изменение почты пользователя на уже зарегистрированную ранее "
                        "возвращает код 403 и сообщение об ошибке")
    def test_change_user_email_to_existing(self, create_user):
        another_user_payload = UserData.create_random_user()
        response = requests.post(Urls.CREATE_USER, json=another_user_payload)
        token = {'Authorization': create_user[1]}
        payload = {"email": another_user_payload["email"]}
        r = requests.patch(Urls.CHANGE_USER_DATA, headers=token, json=payload)
        assert r.status_code == 403 and 'User with such email already exists' in r.text
        # В прошлом спринте попросили добавить удаление созданного пользователя, не знаю насколько это уместно здесь, но сразу сделала
        delete_token = {"Authorization": f"Bearer {response.json()['accessToken']}"}
        requests.delete(Urls.DELETE_USER, headers=delete_token)

    @allure.title("Доступ к данным пользователя без авторизации")
    @allure.description("Запрос данных пользователя без авторизации возвращает код 401 и сообщение об ошибке")
    def test_get_unauthorized_user_data(self):
        r = requests.get(Urls.GET_USER_DATA)
        assert r.status_code == 401 and 'You should be authorised' in r.text

