import allure
from allure_commons.types import Severity
from tests.conftest import podcaster


@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Доступ к статистике автора для владельца')
@allure.title('Доступ к статистике автора для владельца')
@allure.suite('UI Тесты')
def test_access_to_statistik_for_owner(creating_author_api, podcaster_cabinet, deleting_all_authors):
    podcaster.button_to_statistik()
    podcaster.check_on_statistick_page('Статистика автора')
    podcaster.author_settings()


