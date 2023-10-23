import time
from selene import browser
import allure
from allure_commons.types import Severity
from tests.conftest import podcaster

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Снятие эпизода с публикации')
@allure.title('Снятие эпизода с публикации')
@allure.suite('UI Тесты')
def test_unpublishing_episode(creating_episode_api, podcaster_cabinet, deleting_all_authors):
    podcaster.podcast_sidebar_button("It's not me!")
    podcaster.get_in_episode()
    podcaster.button_active_menu_inside_episode()
    podcaster.button_unpublishing_inside_episode()
    podcaster.podcast_sidebar_button('It\'s not me!')
    podcaster.episode_status_unpublished('Черновик')