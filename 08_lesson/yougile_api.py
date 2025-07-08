import requests


class YougileProjectsAPI:
    BASE_URL = "https://ru.yougile.com/api-v2/projects"

    def __init__(self, token):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def create_project(self, data):
        return requests.post(self.BASE_URL, json=data, headers=self.headers)

    def update_project(self, project_id, data):
        url = f"{self.BASE_URL}/{project_id}"
        return requests.put(url, json=data, headers=self.headers)

    def get_project(self, project_id):
        url = f"{self.BASE_URL}/{project_id}"
        return requests.get(url, headers=self.headers)
