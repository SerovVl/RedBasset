import requests


def test_returning_all_members_in_author(getting_token, creating_author_with_image, deleting_all_authors):
    responce = requests.get(
        url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{creating_author_with_image}/members',
        headers={'X-Redtoken': getting_token})
    assert responce.status_code == 200
