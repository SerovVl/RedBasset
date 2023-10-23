from tests.conftest import main_page
from tests.conftest import auth_page
import allure
from allure_commons.types import Severity




@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Авторизация')
@allure.title('Авторизация')
@allure.suite('UI Тесты')
def test_for_authorization(remote_browser):
    with allure.step('Открытие браузера'):
        main_page.open('https://redbasset.tech/')
    with allure.step('Переход на страницу авторизации'):
        main_page.click_log_in_button()
    with allure.step('Заполнение данных для авторизации'):
        auth_page.fill_email('yksyp@mailto.plus')
        auth_page.fill_password('yksyp@mailto.plus')
    with allure.step('Нажатие кнопки "Войти"'):
        auth_page.click_auth_button()
    with allure.step('Проверка что авторизован '):
        main_page.shoud_authorized('yksyp@mailto.plus')
