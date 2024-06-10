import allure
import stellar_burgers_api
import helper
import data


class TestCreateUser:
    @allure.title("Проверка успешности создания пользователя")
    @allure.description("Создание пользователя, проверяем статус ответа и тело ответа")
    def test_success_create_user(self):
        create_user_request = stellar_burgers_api.CreateUserApi.create_user(
            helper.UserFactory.generation_new_user()
        )

        assert (
            create_user_request.status_code == 200
            and create_user_request.json()["user"] is not None
        )

    @allure.title("Проверка регистрации пользователя, который уже зарегистрирован")
    @allure.description(
        "Создаем пользователя, который уже зарегистрирован, проверям статус ответа и тело ответа"
    )
    def test_create_previously_registered_user(self):
        create_user_request = stellar_burgers_api.CreateUserApi.create_user(
            data.TestCreatePreviouslyRegisteredUser.CREATE_USER_BODY
        )

        assert (
            create_user_request.status_code == 403
            and create_user_request.json()
            == data.ResponseBodyText.PREVIOUSLY_REGISTERED_USER
        )

    @allure.title(
        "Проверяем создание пользователя с незаполненными обязательными полями"
    )
    @allure.description(
        "Создаем пользователя с пустым полем email, проверяем статус ответа и тело ответа"
    )
    def test_create_user_with_empty_email(self):
        body = helper.UserFactory.modify_create_user("email", "")
        create_user_request = stellar_burgers_api.CreateUserApi.create_user(body)

        assert (
            create_user_request.status_code == 403
            and create_user_request.json()
            == data.ResponseBodyText.REQUIRED_FIELDS_MISSING
        )
