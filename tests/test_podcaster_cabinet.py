import allure
from allure_commons.types import Severity
from tests.conftest import main_page
from tests.conftest import podcaster

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Возможность перейти в кабинет подкастера')
@allure.title('Возможность перейти в кабинет подкастера')
@allure.suite('UI Тесты')
def test_podcaster_cabinet(authorization):
    with allure.step('Открытие дропдауна в хедере'):
        main_page.header_drop_button()
    with allure.step('Клик по кнопке "Кабинет подкастера"'):
        main_page.to_cabinet_button()
        podcaster.close_monetization()