import requests
from faker import Faker
import allure
import data
import urls


class UserFactory:
    @staticmethod
    @allure.step("Генерация тела для пользователя")
    def generation_new_user():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        return {"email": email, "password": password, "name": name}

    @staticmethod
    @allure.step("Подмена авторизационных данных")
    def modify_create_user(key, value):
        body = data.TestCreatePreviouslyRegisteredUser.CREATE_USER_BODY.copy()
        body[key] = value
        return body

    @staticmethod
    @allure.step("Генерация тела для создания пользователя и возврат логина и пароля")
    def create_user_and_return_login_password():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        payload = {"email": email, "password": password, "name": name}
        requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, data=payload)
        return payload
