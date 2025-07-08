import pytest
from yougile_api import YougileProjectsAPI
from uuid import uuid4


@pytest.fixture(scope="session")
def token():
    # !!! Наставнику: вставьте свой токен здесь !!!
    return "CYzxgIn3n56NxJpuBhc39sBw6FTkFDRdf4kjnkQox-KSqFxC+I7s5Oxw0nwz3tPa"


@pytest.fixture(scope="session")
def api(token):
    return YougileProjectsAPI(token)


@pytest.fixture
def valid_project_data():
    # Используйте реальные ID пользователей вашей команды!
    return {
        "title": f"Test Project {uuid4()}",
        "users": {
            "f3fff726-0d4c-4c16-9b3f-03d530069ee8": "worker"
        }
    }


@pytest.fixture
def invalid_project_data():
    # Нет обязательного поля title
    return {
        "users": {
            "f3fff726-0d4c-4c16-9b3f-03d530069ee8": "worker"
        }
    }
