import requests


def test_deleting_member_from_author(getting_token, creating_author_with_image, adding_member_to_author,
                                     deleting_all_authors):
    response = requests.delete(
        url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{creating_author_with_image}/role/655',
        headers={'X-Redtoken': getting_token})
    assert response.status_code == 204
