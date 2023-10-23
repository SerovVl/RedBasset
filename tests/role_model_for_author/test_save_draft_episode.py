import time
import allure
from allure_commons.types import Severity
from tests.conftest import podcaster

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Создание черновика эпизода')
@allure.title('Создание черновика эпизода')
@allure.suite('UI Тесты')
def test_save_draft_episode(creating_podcast_api, podcaster_cabinet, deleting_all_authors):
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
    with allure.step('Сохранить черновик'):
        podcaster.button_save_draft()
        time.sleep(2)
    with allure.step('Проверка что черновик создан'):
        podcaster.podcast_sidebar_button('It\'s not me!')
        podcaster.episode_status_unpublished('Черновик')
