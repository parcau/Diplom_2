# Diplom_2
Задание 2: API
В папке tests расположены все тесты:
test_create_order - тесты с проверкой создания заказа; с авторизированным пользователем и нет;
с игредиентами и без них; с неверным хешем ингредиентов
test_create_user - тесты с проверкой создания уникального пользователя; пользователя, который
уже ранее зарегистрирован; с незаполненнным обязательным полем email
test_get_list_orders - тестф с запросом списка заказов конкретного пользователя с авторизацией и без
test_login_user - тесты с проверкой авторизации пользователя существующего и с неверным логином и паролем
test_update_user - тесты с проверкой изменения данных пользователя с авторизацией и без