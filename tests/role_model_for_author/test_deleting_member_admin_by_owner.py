import time

from tests.conftest import podcaster
import allure
from allure_commons.types import Severity

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Удаление участника с ролью "Администратор" из автора')
@allure.title('Удаление участника с ролью "Администратор" из автора')
@allure.suite('UI Тесты')
def test_deleting_member_admin_by_owner(creating_author_api, admin_auth_api, podcaster_cabinet, deleting_all_authors):
    with allure.step('Переход в таб "Участники"'):
        podcaster.members_button()
        time.sleep(2)
    with allure.step('Нажатие кнопки значка удалить участника'):
        podcaster.deleteting_member()
    with allure.step('Подтверждение удаления участника'):
        podcaster.confirm_deleting_member()