import requests
from tests_api.paths import get_path_to_file


def test_adding_image_to_author(getting_token, creating_author, deleting_all_authors):
    url = f"https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{creating_author}/icon"
    payload = {}
    files = {'file': open(get_path_to_file('img/qa-dev.png'), 'rb')}
    headers = {
        'accept': 'application/json',
        'X-RedToken': getting_token
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    assert response.status_code == 200
