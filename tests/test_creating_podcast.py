from tests.conftest import podcaster


def test_creating_podcast(creating_author):
    podcaster.click_creating_podcast()
    podcaster.fill_podcast_name('It\'s not me!')
    podcaster.fill_description_podcast('Этот подкаст создан с помощью автоматизированного ПО. '
                                       'Данное поле вмещает до 600 символов. '
                                       'Так же в данное поле можно ввести спецсимволы,'
                                       ' такие как: "!@#$%^&*()_+}{"|?"')
    podcaster.upload_podcast_image('img/QA.jpeg')
    podcaster.click_settings_podcast()
    podcaster.choose_category('Досуг')
    podcaster.choose_subcategory('Анимация и манга')
    podcaster.add_category()
    podcaster.choose_category('Бизнес')
    podcaster.choose_subcategory('Маркетинг')
    podcaster.choose_language('Русский')
    podcaster.next_page()
    podcaster.subtit_creating_podcast()
    podcaster.shoul_exist_podcast('It\'s not me!')

