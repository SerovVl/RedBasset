import requests


def test_adding_member_to_author(getting_token, creating_author_with_image, deleting_all_authors):
    response = requests.post(
        url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{creating_author_with_image}/role',
        json={
            "email": "levix41181@mugadget.com",
            "role": "ADMIN"
        },
        headers={'X-Redtoken': getting_token})
    assert response.status_code == 204
