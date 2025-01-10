from faker import Faker

class UserData:

    data_correct = {
        "email": 'Pakhatinskaya151@yandex.ru',
        "password": 'abcabc'}

    data_incorrect = {
        "email": 'Pakhatinskaya1515@yandex.ru',
        "password": 'adcadc'}

    data_double = {
        "email": 'Pakhatinskaya151@yandex.ru',
        "password": 'abcabc',
        "name": 'Валентина'}

    data_with_empty_email = {
        "email": '',
        "password": 'abcabc',
        "name": 'Валентина'}

    data_with_empty_password = {
        "email": 'Pakhatinskaya151@yandex.ru',
        "password": '',
        "name": 'Валентина'}

    data_with_empty_name = {
        "email": 'Pakhatinskaya151@yandex.ru',
        "password": 'abcabc',
        "name": ''}

    data_updated = {
        "email": 'Pakhatinskaya151@yandex.ru',
        "password": 'abcabc',
        "name": 'Валентина'}

    @staticmethod
    def create_random_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

class OrderData:
    data_for_correct_order = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72"]
    }

    data_for_incorrect_order = {
        "ingredients": ["60d3b41abdacab0026a733c6g", "609646e4dc916e00276b2870g"]}

