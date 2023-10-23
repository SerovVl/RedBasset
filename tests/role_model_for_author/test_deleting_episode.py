import time

import allure
from allure_commons.types import Severity
from tests.conftest import podcaster

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Удаление эпизода')
@allure.title('Удаление эпизода')
@allure.suite('UI Тесты')
def test_deleting_episode(creating_episode_api, podcaster_cabinet, deleting_all_authors):
    podcaster.podcast_sidebar_button('It\'s not me!')
    podcaster.get_in_episode()
    podcaster.button_active_menu_inside_episode()
    podcaster.button_deleting_episode_inside_episode()
    podcaster.button_confirm_deleting_episode()
    podcaster.check_no_episodes('Здесь пока нет ни одного выпуска, вы')
