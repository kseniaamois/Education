# --- [POST] /api-v2/projects ---


def test_create_project_positive(api, valid_project_data):
    """Позитивный: создание проекта с валидными данными"""
    response = api.create_project(valid_project_data)
    print("POST positive:", response.status_code, response.json())
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_create_project_negative(api, invalid_project_data):
    """Негативный: создание проекта без обязательного поля title"""
    response = api.create_project(invalid_project_data)
    print("POST negative:", response.status_code, response.json())
    assert response.status_code in (400, 422)


# --- [GET] /api-v2/projects/{id} ---


def test_get_project_positive(api, valid_project_data):
    """Позитивный: получение существующего проекта"""
    create_resp = api.create_project(valid_project_data)
    project_id = create_resp.json()["id"]
    response = api.get_project(project_id)
    print("GET positive:", response.status_code, response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["title"] == valid_project_data["title"]


def test_get_project_negative(api):
    """Негативный: получение проекта по несуществующему id"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(fake_id)
    print("GET negative:", response.status_code, response.json())
    assert response.status_code == 404


# --- [PUT] /api-v2/projects/{id} ---


def test_update_project_positive(api, valid_project_data):
    """Позитивный: обновление существующего проекта"""
    create_resp = api.create_project(valid_project_data)
    project_id = create_resp.json()["id"]
    update_data = {
        "title": "Updated Project",
        "users": valid_project_data["users"]
    }
    response = api.update_project(project_id, update_data)
    print("PUT positive:", response.status_code, response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id


def test_update_project_negative(api):
    """Негативный: обновление проекта по несуществующему id"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    update_data = {
        "title": "Updated Project",
        "users": {
            "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
        }
    }
    response = api.update_project(fake_id, update_data)
    print("PUT negative:", response.status_code, response.json())
    assert response.status_code == 404 or response.status_code == 400
