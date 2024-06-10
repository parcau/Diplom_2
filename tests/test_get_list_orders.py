import allure
import data
import stellar_burgers_api


class TestGetListOrders:
    @allure.title("Получаем список конкретного пользователя с авторизацией")
    @allure.description(
        "Авторизируемся и получаем список заказов, проверяем статус ответа и тело ответа"
    )
    def test_get_list_orders_with_auth(self):
        auth_user = stellar_burgers_api.AuthUserApi.login_user(
            data.TestLoginUser.TEST_USER_BODY
        )
        token = auth_user.json()["accessToken"]
        get_list_orders = stellar_burgers_api.GetListOrdersApi.get_list_orders(token)

        assert (
            get_list_orders.status_code == 200
            and get_list_orders.json()["orders"] is not None
        )

    @allure.title("Получаем список конкретного пользователя без авторизации")
    @allure.description(
        "Получаем список заказов без авторизацииБ проверяем статус ответа и тело ответа"
    )
    def test_get_list_without_auth(self):
        token = ""
        get_list_orders = stellar_burgers_api.GetListOrdersApi.get_list_orders(token)

        assert (
            get_list_orders.status_code == 401
            and get_list_orders.json() == data.ResponseBodyText.UNAUTHORIZATED_USER
        )
