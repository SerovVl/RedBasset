import time
import allure
from tests.conftest import podcaster
import allure
from allure_commons.types import Severity


@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Публикация эпизода с отложенной публикацией')
@allure.title('Публикация эпизода с отложенной публикацией')
@allure.suite('UI Тесты')
def test_publishing_delay_episode(creating_podcast_api, podcaster_cabinet, deleting_all_authors):
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
    with allure.step('Установка даты отложенной публикации'):
        podcaster.date_episode_delay('18')
    with allure.step('Установка времени отложенной публикации'):
        podcaster.time_episode_delay('13', '00')
    with allure.step('Публикация эпизода'):
        podcaster.publish_episode()
    with allure.step('Открытие активного меню внутри эпизода'):
        podcaster.button_active_menu_inside_episode()
    with allure.step('Нажатие опубликовать эпизод'):
        podcaster.button_publishing_inside_episode()