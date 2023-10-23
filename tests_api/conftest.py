import os
import json
import requests
import pytest
import tests_api
from paths import get_path_to_file


@pytest.fixture()
def getting_token():
    payload = {
        "userName": "RedBassTest@gmail.com",
        "password": "Qwerty11"}

    response = requests.post(
        url='https://podcaster-service-api.stage.redbasset.tech/_api/rest/auth/auth',
        json=payload)

    data = response.json()
    access_token = data['accessToken']
    return access_token


@pytest.fixture()
def creating_author(getting_token):
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
    return author_id


@pytest.fixture()
def creating_author_with_image(getting_token):
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

    # Загрузка изображения для автора
    url = f"https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{author_id}/icon"
    payload = {}
    files = {'file': open(get_path_to_file('img/qa-dev.png'), 'rb')}
    headers = {
        'accept': 'application/json',
        'X-RedToken': getting_token
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    return author_id


@pytest.fixture()
def creating_podcast(getting_token, creating_author):
    url = 'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/podcast'
    data = {
        "podcast": {
            "name": "It's not me!",
            "description": "My rocking podcast",
            "category": "TV & Film",
            "subcategory": "Film History",
            "language": "RU",
            "alias": "my-mega-alias",
            "explicit": False,
            "author": {
                "authorId": creating_author
            }
        }
    }
    headers = {'X-Redtoken': getting_token}
    # Создание подкаста
    response = requests.post(url=url,
                             json=data,
                             headers=headers)
    data = response.json()
    print(data)
    podcast_id = data['podcastId']

    # Загрузка изображения для подкаста
    url = f"https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/podcast/{podcast_id}/cover"
    payload = {}
    files = {'file': open(get_path_to_file('img/qa-dev.png'), 'rb')}
    headers = {
        'accept': 'application/json',
        'X-RedToken': getting_token
    }
    response = requests.post(url, headers=headers, data=payload, files=files)
    print(response.text)
    return podcast_id


@pytest.fixture()
def deleting_all_authors(getting_token):
    yield
    response = requests.get(url='https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author',
                            headers={'X-Redtoken': getting_token})
    data = response.json()
    # author_id = data['authors'][0]['authorId']
    author_ids = [author['authorId'] for author in data['authors']]
    print(author_ids)

    for author_id in author_ids:
        response = requests.delete(
            url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{author_id}',
            headers={'X-Redtoken': getting_token})
    print(response.text)
    return author_ids


@pytest.fixture()
def adding_member_to_author(getting_token, creating_author_with_image):
    response = requests.post(
        url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/author/{creating_author_with_image}/role',
        json={
            "email": "levix41181@mugadget.com",
            "role": "ADMIN"
        },
        headers={'X-Redtoken': getting_token})
    assert response.status_code == 204


@pytest.fixture()
def adding_member_to_podcast(getting_token, creating_podcast, deleting_all_authors):
    response = requests.post(
        url=f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/podcast/{creating_podcast}/role',
        json={
            "email": "levix41181@mugadget.com",
            "role": "ADMIN"
        },
        headers={'X-Redtoken': getting_token})
    assert response.status_code == 204

@pytest.fixture()
def importing_podcast(getting_token, creating_author):
    rss = 'https://redbasset.tech/_api/rest/podcast_rss/1146'
    url = f'https://podcaster-service-api.stage.redbasset.tech/_api/rest/podcaster/podcast/import?rssUrl={rss}&authorId={creating_author}'
    headers = {'X-Redtoken': getting_token}
    response = requests.post(url=url, headers=headers)
    data = response.json()
    podcast_id = data['savedPodcastId']
    return podcast_id
