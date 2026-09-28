from enum import Enum


class AllureEpic(str, Enum):
    LMS = "LMS service" # LMS (система управления обучением)
    STUDENT = "Student service"
    ADMINISTRATION = "Administration service"
