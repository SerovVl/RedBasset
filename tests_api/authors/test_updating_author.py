import requests
from tests_api import paths


def test_updating_author_api(getting_token, creating_author_with_image, deleting_all_authors):
    response = requests.post(
        url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{creating_author_with_image}',
        json={
            "author": {
                "id": creating_author_with_image,
                "name": "New author name",
                "description": "My author",
                "email": "my72305@email.ru",
                "phone": "8002008000"
            }
        },
        headers={'X-Redtoken': getting_token})
    assert response.status_code == 200
