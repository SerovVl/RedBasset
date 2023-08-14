import time

import allure

from tests.conftest import podcaster


def test_creating_episode(creating_podcast):
    with allure.step('Переход на страницу подкаста'):
        podcaster.podcast_sidebar_button("It's not me!")

    with allure.step('Нажатие кнопки "Новый выпуск"'):
        podcaster.creating_episode_button()

    with allure.step('Загрузка файла'):
        podcaster.upload_episode(
            'audio/News.mp3')

    with allure.step('Заполнение поля "Название эпизода"'):
        podcaster.fill_episode_name('Как начинающему разработчику найти работу')

    with allure.step('Заполнение поля "Описание"'):
        podcaster.fill_episode_description(
            'Разбираемся, как можно получить свою первую работу в IT в качестве junior фронтенд-разработчика '
            'вместе с Алексеем Авдеевым, CTO в Mish, и Владиславом Соколенко, разработчиком в Mish')

    with allure.step('Переход в таб "Настройки"'):
        podcaster.settings_button_tab()

    with allure.step('Заполнение поля "Номер сезона"'):
        podcaster.season_number('1')

    with allure.step('Заполнение поля "Номер эпизода"'):
        podcaster.episode_number('1')

    with allure.step('Выбор типа выпуска'):
        podcaster.episode_type('Бонусный')

    with allure.step('Содержание ненормативной лексики'):
        podcaster.obscene_language('Да, присутствует')

    with allure.step('Публикация эпизода'):
        podcaster.publish_episode()

