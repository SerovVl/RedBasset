import allure
from allure_commons.types import Severity
import time
from tests.conftest import main_page
from tests.conftest import podcaster


@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Удаление подкаста')
@allure.title('Удаление подкаста')
@allure.suite('UI Тесты')
def test_deleting_podcast(creating_podcast_api, podcaster_cabinet, deleting_all_authors):
    with allure.step('Переход к списку подкастов'):
        podcaster.main_author_page('AQA Тест 123')
    with allure.step('Удаление подкаста'):
        podcaster.delete_podcast()
