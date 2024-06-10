import allure
import data
import stellar_burgers_api
import helper


class TestUpdateUser:
    @allure.title("Проверяем обновления информации о пользователе авторизовавшись")
    @allure.description(
        "Создаем нового пользователя, авторизуемся, изменяем данные пользователя, проверяем статус кода и тело ответа"
    )
    def test_update_auth_user(self):
        login_pass = helper.UserFactory.create_user_and_return_login_password()
        auth_user = stellar_burgers_api.AuthUserApi.login_user(login_pass)
        token = auth_user.json()["accessToken"]
        update_user = stellar_burgers_api.UpdateUserApi.update_user(token)
        stellar_burgers_api.AuthUserApi.delete_user(token)

        assert (
            update_user.status_code == 200
            and update_user.json() == data.ResponseBodyText.UPDATE_USER
        )

    @allure.title("Проверяем обновление информации о пользователе не авторизовавшись")
    @allure.description(
        "Обновляем данные пользователя, проверяем статус ответа и код ответа"
    )
    def test_update_unauth_user(self):
        token = ""
        update_user = stellar_burgers_api.UpdateUserApi.update_user(token)

        assert (
            update_user.status_code == 401
            and update_user.json() == data.ResponseBodyText.UNAUTHORIZATED_USER
        )
