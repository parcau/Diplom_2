import requests
import data
import urls
import allure


class CreateUserApi:
    @staticmethod
    @allure.step("Отправка запроса на создание пользователя")
    def create_user(body):
        return requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, json=body)


class AuthUserApi:
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(login_pass):
        return requests.post(urls.BASE_URL + urls.LOGIN_USER_ENDPOINT, json=login_pass)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        return requests.delete(
            urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers={"Authorization": token}
        )


class UpdateUserApi:
    @staticmethod
    @allure.step("Обновляем данные пользователя")
    def update_user(token):
        body = data.TestUpdateUser.NEW_USER_BODY
        return requests.patch(
            urls.BASE_URL + urls.UPDATE_USER_ENDPOINT,
            json=body,
            headers={"Authorization": token},
        )


class CreateOrderApi:
    @staticmethod
    @allure.step("Создаем заказ")
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)


class GetListOrdersApi:
    @staticmethod
    @allure.step("Создаем запрос на список заказов")
    def get_list_orders(token):
        return requests.get(
            urls.BASE_URL + urls.GET_LIST_ORDERS_ENDPOINT,
            headers={"Authorization": token},
        )
