import requests
from tests_api import paths


def test_deleting_author(getting_token, creating_author_with_image):
    response = requests.get(url='https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author',
                            headers={'X-Redtoken': getting_token})
    data = response.json()
    author_ids = [author['authorId'] for author in data['authors']]
    print(author_ids)

    for author_id in author_ids:
        response = requests.delete(
            url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{author_id}',
            headers={'X-Redtoken': getting_token})
    print(response.text)
    assert response.status_code == 204