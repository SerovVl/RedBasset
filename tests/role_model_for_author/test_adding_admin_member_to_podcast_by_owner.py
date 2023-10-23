import time
from tests.conftest import podcaster
import allure
from allure_commons.types import Severity

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Добавление "Владельца" в участники подкаста владельцем')
@allure.title('Добавление "Владельца" в участники подкаста владельцем')
@allure.suite('UI Тесты')
def test_adding_admin_member_to_podcast_by_owner(creating_podcast_api, podcaster_cabinet, deleting_all_authors):
    with allure.step('Переход на страницу подкаста'):
        podcaster.podcast_sidebar_button("It's not me!")
    with allure.step('Переход в таб "Участники"'):
        podcaster.podcast_members_button()
    with allure.step('Нажатие кнопки "Добавить участника"'):
        podcaster.button_adding_members_in_podcast()
    with allure.step('Ввод email в поле "Email"'):
        podcaster.email_input_member('addbys@mailto.plus')
    with allure.step('Выбор роли участника'):
        podcaster.choose_role_member('Владелец')
    with allure.step('Подтверждение добавления участника'):
        podcaster.add_member()