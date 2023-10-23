import requests


def test_returning_all_authors(getting_token, creating_author_with_image, deleting_all_authors):
    response = requests.get(url='https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author',
                            headers={'X-Redtoken': getting_token})
    print(response.json())
    assert response.status_code == 200
