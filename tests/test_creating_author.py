import time

import allure

from tests.conftest import podcaster


def test_creating_author(podcaster_cabinet):
    with allure.step('Нажатие кнопки "Создание автора"'):
        podcaster.click_creating_author()

    with allure.step('Загрузка обложки автора'):
        podcaster.upload_image('img/Mona_Lisa1.jpg')

    with allure.step('Заполнение поля имя автора'):
        podcaster.fill_author_name('AQA Тест 123')

    with allure.step('Заполнение поля описание автора'):
        podcaster.fill_author_description('По своей сути рыбатекст является альтернативой традиционному '
                                          'lorem ipsum, который вызывает у некторых людей недоумение при '
                                          'попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба '
                                          'на русском языке наполнит любой макет непонятным смыслом и придаст '
                                          'неповторимый колорит советских времен. '
                                          'Вы можете добавить в данное  поле до 600 символов!')

    with allure.step('Переход в "Дополнительное"'):
        podcaster.additional_about_author()

    with allure.step('Заполнение поля "Email"'):
        podcaster.fill_additional_email('yksyp@mailto.plus')

    with allure.step('Заполнение поля "Телефон"'):
        podcaster.fill_additional_phone('88005553535')

    with allure.step('Нажатие кнопки "Создать автора"'):
        podcaster.submit_button()

    with allure.step('Проверка что автор существует'):
        podcaster.shoul_exist_author('AQA Тест 123')

