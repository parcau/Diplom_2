class TestCreatePreviouslyRegisteredUser:
    CREATE_USER_BODY = {
        "email": "registered@mail.ru",
        "password": "123456",
        "name": "Ivan",
    }


class TestLoginUser:
    TEST_USER_BODY = {"email": "markov7777@yandex.ru", "password": "123456789"}


class TestUpdateUser:
    NEW_USER_BODY = {"email": "newemail@new.ru", "name": "New Name"}


class TestCreateOrder:
    TEST_INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa73"]
    }
    TEST_INGREDIENTS2 = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa74"]
    }
    GALACTIC_BURGER = "Традиционный-галактический краторный бургер"
    SPACE_BURGER = "Space флюоресцентный бургер"


class ResponseBodyText:
    PREVIOUSLY_REGISTERED_USER = {"message": "User already exists", "success": False}
    REQUIRED_FIELDS_MISSING = {
        "message": "Email, password and name are required fields",
        "success": False,
    }
    INCORRECT_EMAIL = {"message": "email or password are incorrect", "success": False}
    UPDATE_USER = {
        "success": True,
        "user": {"email": "newemail@new.ru", "name": "New Name"},
    }
    UNAUTHORIZATED_USER = {"message": "You should be authorised", "success": False}
    MISSING_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided",
    }
