import allure
from allure_commons.types import Severity
import time
from tests.conftest import main_page
from tests.conftest import podcaster


@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Удаление автора')
@allure.title('Удаление автора')
@allure.suite('UI Тесты')
def test_deleting_author(creating_author_api, podcaster_cabinet_test):
    with allure.step('Переход в таб "Настройки"'):
        podcaster.author_settings()
    with allure.step('Удаление автора'):
        podcaster.delete_author()
        time.sleep(10)
    with allure.step('Проверка что автора нет'):
        podcaster.main_author_page_hiden()
