import allure
import data
import stellar_burgers_api


class TestCreateOrder:
    @allure.step("Проверяем создание заказа с авторизацией")
    @allure.description(
        "Авторизируемся, создаем заказ, проверяем статус ответа и тело ответа"
    )
    def test_create_order_by_login(self):
        body = data.TestCreateOrder.TEST_INGREDIENTS
        stellar_burgers_api.AuthUserApi.login_user(data.TestLoginUser.TEST_USER_BODY)
        create_order = stellar_burgers_api.CreateOrderApi.create_order(body)

        assert (
            create_order.status_code == 200
            and create_order.json()["name"] == data.TestCreateOrder.SPACE_BURGER
            and create_order.json()["order"] is not None
        )

    @allure.step("Проверяем создание заказа без авторизации")
    @allure.description(
        "Создаем заказ без авторизации, проверяем статус ответа и тело ответа"
    )
    def test_create_order_not_login(self):
        body = data.TestCreateOrder.TEST_INGREDIENTS2
        create_order = stellar_burgers_api.CreateOrderApi.create_order(body)

        assert (
            create_order.status_code == 200
            and create_order.json()["name"] == data.TestCreateOrder.GALACTIC_BURGER
            and create_order.json()["order"] is not None
        )

    @allure.step("Проверяем создание заказа без ингредиентов")
    @allure.description(
        "Создаем заказ без ингредиентов, проверяем статус ответа и тело ответа"
    )
    def test_create_order_without_ingredients(self):
        body = {}
        create_order = stellar_burgers_api.CreateOrderApi.create_order(body)

        assert (
            create_order.status_code == 400
            and create_order.json() == data.ResponseBodyText.MISSING_INGREDIENTS
        )

    @allure.step("Проверяем создание заказа с неверным хемем ингредиентов")
    @allure.description(
        "Создаем заказ с неверным хешем ингредиентов, проверяем статус ответа и тело ответа"
    )
    def test_create_order_with_incorrect_hash_ingredients(self):
        body = {"ingredients": ["61c0c5a71d1f82001bdxxx6d", "609646e4dc916e35776b2870"]}
        create_order = stellar_burgers_api.CreateOrderApi.create_order(body)

        assert (
            create_order.status_code == 500
            and "Internal Server Error" in create_order.text
        )
