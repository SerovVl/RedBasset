import requests
from tests_api import paths


def test_creating_author(getting_token, deleting_all_authors):
    # Создание автора
    response = requests.post(url='https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author',
                             json={
                                 "author": {
                                     "name": "AQA Тест 123",
                                     "description": "My author",
                                     "email": "my@email.ru",
                                     "phone": "8002008000"
                                 }
                             },
                             headers={'X-Redtoken': getting_token})
    data = response.json()
    author_id = data['authorId']
    assert response.status_code == 200
    # Загрузка изображения для автора
    url = f"https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{author_id}/icon"
    payload = {}
    files = {'file': open(paths.get_path_to_file('img/qa-dev.png'), 'rb')}
    headers = {
        'accept': 'application/json',
        'X-RedToken': getting_token
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    assert response.status_code == 200
