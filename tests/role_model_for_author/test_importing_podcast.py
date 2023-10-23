import allure
from allure_commons.types import Severity
from tests.conftest import podcaster

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Импорт подкаста')
@allure.title('Импорт подкаста')
@allure.suite('UI Тесты')
def test_importind_podcast(creating_author_api, podcaster_cabinet, deleting_all_authors):
    with allure.step('Нажатие кнопки "Ипорт"'):
        podcaster.import_button()
    with allure.step('Ввод ссылки на RSS-канал'):
        podcaster.import_input('https://redbasset.tech/_api/rest/podcast_rss/1146')
    with allure.step('Нажатие кнопки "Найти подкаст"'):
        podcaster.search_by_rss()
    with allure.step('Нажатие кнопки "Начать импорт"'):
        podcaster.start_import()

    podcaster.close_monetization()