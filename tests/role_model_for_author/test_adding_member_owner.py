import time

from tests.conftest import podcaster
import allure
from allure_commons.types import Severity

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Добавление "Владельца" в участники')
@allure.title('Добавление "Владельца" в участники')
@allure.suite('UI Тесты')
def test_adding_member_owner(creating_author_api, podcaster_cabinet, deleting_all_authors):
    with allure.step('Переход в таб "Участники"'):
        podcaster.members_button()
    with allure.step('Нажатие кнопки "Добавить участника"'):
        podcaster.adding_member_button()
    with allure.step('Ввод email в поле "Email"'):
        podcaster.email_input_member('tokar.nnov@yandex.ru')
    with allure.step('Выбор роли участника'):
        podcaster.choose_role_member('Владелец')
    with allure.step('Подтверждение добавления участника'):
        podcaster.add_member()