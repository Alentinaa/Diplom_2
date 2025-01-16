import pytest
import requests
from data import UserData
from urls import Urls

@pytest.fixture(scope="function")
def create_user():
    payload = UserData.create_random_user()
    response = requests.post(Urls.CREATE_USER, data=payload)
    token = response.json().get('accessToken')
    if not token:
        pytest.fail("Ошибка: accessToken не найден в ответе.")
    yield response, token, payload
    requests.delete(Urls.DELETE_USER, headers={'Authorization': f'Bearer {token}'})

@pytest.fixture(scope="function")
def create_second_user():
    payload = UserData.create_random_user()
    response = requests.post(Urls.CREATE_USER, json=payload)
    token = response.json().get('accessToken')
    if not token:
        pytest.fail("Ошибка: accessToken не найден в ответе второго пользователя.")
    yield response, token, payload
    requests.delete(Urls.DELETE_USER, headers={'Authorization': f'Bearer {token}'})
