import allure
import data
import helper
import stellar_burgers_api


class TestAuthUser:
    @allure.step("Проверяем успешную авторизацию пользователя")
    @allure.description(
        "Создаем польpователя, авторизуемся, проверяем статус ответа и тело ответа, удаляем пользователя"
    )
    def test_login_user(self):
        login_pass = helper.UserFactory.create_user_and_return_login_password()
        auth_user = stellar_burgers_api.AuthUserApi.login_user(login_pass)
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.AuthUserApi.delete_user(token)

        assert auth_user.status_code == 200 and auth_user.json()["user"] is not None

    @allure.step("Проверяем авторизацию с неверным email")
    @allure.description(
        "Вводим несуществующий email, проверяем статус ответа и тело ответа"
    )
    def test_login_incorrect_email(self):
        body = helper.UserFactory.modify_create_user(
            "email", "pochta_kotoroi_net@mamuka.ru"
        )
        auth_user = stellar_burgers_api.AuthUserApi.login_user(body)

        assert (
            auth_user.status_code == 401
            and auth_user.json() == data.ResponseBodyText.INCORRECT_EMAIL
        )
