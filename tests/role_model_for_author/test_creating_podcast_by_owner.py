import allure
from allure_commons.types import Severity
from tests.conftest import podcaster

@allure.label("owner", "Владимир С.")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.story('Создание подкаста владельцем')
@allure.title('Создание подкаста владельцем')
@allure.suite('UI Тесты')
def test_creating_podcast_by_owner(creating_author_api, podcaster_cabinet, deleting_all_authors):
    with allure.step('Нажатие кнопки "Создать подкаст"'):
        podcaster.click_creating_podcast()
    with allure.step('Заполнение поля "Название подкаста"'):
        podcaster.fill_podcast_name('It\'s not me!')
    with allure.step('Заполнение поля "Описание подкаста"'):
        podcaster.fill_description_podcast('Этот подкаст создан с помощью автоматизированного ПО. '
                                       'Данное поле вмещает до 600 символов. '
                                       'Так же в данное поле можно ввести спецсимволы,'
                                       ' такие как: "!@#$%^&*()_+}{"|?"')
    with allure.step('Загрузка обложки подкаста'):
        podcaster.upload_podcast_image('img/QA.jpeg')
    with allure.step('Переход на вкладку "Настройки" подкаста'):
        podcaster.click_settings_podcast()
    with allure.step('Выбор категории подкаста'):
        podcaster.choose_category('Досуг')
    with allure.step('Выбор субкатегории подкаста'):
        podcaster.choose_subcategory('Анимация и манга')
    with allure.step('Кнопка "+ Добавить категорию"'):
        podcaster.add_category()
    with allure.step('Выбор категории подкаста'):
        podcaster.choose_category('Бизнес')
    with allure.step('Выбор субкатегории подкаста'):
        podcaster.choose_subcategory('Маркетинг')
    with allure.step('Выбор языка подкаста'):
        podcaster.choose_language('Русский')
    with allure.step('Переход на вкладку "Дополнительное" подкаста'):
        podcaster.next_page()
    with allure.step('Подтверждение создания подкаста'):
        podcaster.subtit_creating_podcast()
    with allure.step('Проверка что подкаст создан'):
        podcaster.shoul_exist_podcast('It\'s not me!')


