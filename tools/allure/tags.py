from enum import Enum


class AllureTag(str, Enum):
    USERS = "USERS"
    FILES = "FILES"
    COURSES = "COURSES"
    EXERCISES = "EXERCISES"
    REGRESSION = "REGRESSION"
    AUTHENTICATION = "AUTHENTICATION"

    GET_ENTITY = "GET_ENTITY"
    GET_ENTITIES = "GET_ENTITIES"
    CREATE_ENTITY = "CREATE_ENTITY"
    UPDATE_ENTITY = "UPDATE_ENTITY"
    DELETE_ENTITY = "DELETE_ENTITY"
    VALIDATE_ENTITY = "VALIDATE_ENTITY"


"""
Теги нужны для фильтрации автотестов в Allure отчёте.
По умолчанию автотесты в Allure отчете содержат теги, которые берутся из pytest маркировок:
@pytest.mark.users, @pytest.mark.regression и т.п.
Все зависит от договоренности по тегам на проекте.
пример тега через allure @allure.tag("USERS", "REGRESSION")
"""