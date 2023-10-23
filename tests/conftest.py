import requests
import pytest
from selene import browser
import time
from tests import paths
from pages.authentication_page import AuthPage
from pages.main_site_page import MainPage
from pages.podcasters_page import PodcasterPage
from selenium import webdriver
from utils import attach

main_page = MainPage()
auth_page = AuthPage()
podcaster = PodcasterPage()


@pytest.fixture(scope='function', autouse=True)
def remote_browser():
    capabilities = {
        "browserName": 'chrome',
        "browserVersion": '114.0',
        'enableVNC': True,
        'enableVideo': True,
        'screenResolution': '1920x1080x24',
        'sessionTimeout': '8m'
    }
    options = webdriver.ChromeOptions()
    options.set_capability('selenoid:options', capabilities)
    driver = webdriver.Remote(command_executor='https://selenoid.../wd/hub', options=options)

    browser.config.driver = driver
    driver.maximize_window()
    yield driver
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    driver.quit()


def getting_token():
    payload = {
        "userName": "yksyp@mailto.plus",
        "password": "yksyp@mailto.plus"}

    response = requests.post(
        url='https://redbasset.tech/*',
        json=payload)

    data = response.json()
    access_token = data['accessToken']
    return access_token


@pytest.fixture()
def creating_author_api():
    # Создание автора
    response = requests.post(url='https://redbasset.tech/*',
                             json={
                                 "author": {
                                     "name": "AQA Тест 123",
                                     "description": "My author",
                                     "email": "my@email.ru",
                                     "phone": "8002008000"
                                 }
                             },
                             headers={'X-Redtoken': getting_token()})
    data = response.json()
    author_id = data['authorId']
    return author_id


@pytest.fixture()
def deleting_all_authors():
    yield
    response = requests.get(url='https://redbasset.tech/*',
                            headers={'X-Redtoken': getting_token()})

    data = response.json()
    author_ids = [author['authorId'] for author in data['authors']]
    for author_id in author_ids:
        response = requests.delete(url=f'https://redbasset.tech/*/{author_id}',
                                   headers={'X-Redtoken': getting_token()})
    print(response.text)


@pytest.fixture()
def creating_podcast_api(creating_author_api):
    # Создание подкаста
    response = requests.post(url='https://redbasset.tech/*',
                             json={
                                 "podcast": {
                                     "name": "It's not me!",
                                     "description": "My rocking podcast",
                                     "category": "TV & Film",
                                     "subcategory": "Film History",
                                     "language": "RU",
                                     "alias": "my-mega-alias",
                                     "explicit": False,
                                     "author": {
                                         "authorId": int(creating_author_api)
                                     }
                                 }
                             },
                             headers={'X-Redtoken': getting_token()})
    data = response.json()
    podcast_id = data['podcastId']

    # Загрузка изображения для подкаста
    url = f"https://redbasset.tech/*/{podcast_id}/cover"
    payload = {}
    files = {'file': open(paths.get_path_to_file('img/Mona_Lisa1.jpg'), 'rb')}
    headers = {
        'accept': 'application/json',
        'X-RedToken': 'c5c0c8b5-8f20-4447-a31c-9eedc1631033'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    return podcast_id


@pytest.fixture()
def authorization(remote_browser):
    main_page.open('https://redbasset.tech/')
    main_page.click_log_in_button()
    auth_page.fill_email('yksyp@mailto.plus')
    auth_page.fill_password('yksyp@mailto.plus')
    auth_page.click_auth_button()
    time.sleep(2)


@pytest.fixture()
def podcaster_cabinet(authorization):
    main_page.header_drop_button()
    main_page.to_cabinet_button()
    podcaster.close_monetization()
    yield
    podcaster.main_author_page('AQA Тест 123')
    time.sleep(1)


@pytest.fixture()
def podcaster_cabinet_test(authorization):
    main_page.header_drop_button()
    main_page.to_cabinet_button()
    podcaster.close_monetization()


@pytest.fixture()
def creating_episode_api(creating_podcast_api):
    # Создание эпизода
    response = requests.post(url='https://redbasset.tech/*',
                             json={
                                 "episode": {
                                     "name": "Как начинающему разработчику найти работу",
                                     "description": "Разбираемся, как можно получить свою первую работу в IT"
                                                    " в качестве junior фронтенд-разработчика вместе с Алексеем Авдеевым,"
                                                    " CTO в Mish, и Владиславом Соколенко, разработчиком в Mish",
                                     "episodeNumber": 1,
                                     "seasonNumber": 1,
                                     "episodeType": "full",
                                     "podcastId": int(creating_podcast_api),
                                     "monetized": False,
                                     "explicit": True
                                 }
                             },
                             headers={'X-Redtoken': getting_token()})
    data = response.json()
    episode_id = data['episodeId']

    # Загрузка файла для эпизода
    url = f"https://redbasset.tech/*/{episode_id}/file"
    payload = {}
    files = {'file': open(paths.get_path_to_file('audio/News.mp3'), 'rb')}
    headers = {
        'accept': 'application/json',
        'X-RedToken': 'c5c0c8b5-8f20-4447-a31c-9eedc1631033'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

    # Публикация эпизода
    response = requests.post(url=f'https://redbasset.tech/*/{episode_id}',
                             json={
                                 'episode': {
                                     'published': True
                                 },
                             },
                             headers={'X-Redtoken': getting_token()})
    print(response.text)
    return episode_id
