import time

import allure
from tests.conftest import main_page
from tests.conftest import podcaster

def test_podcaster_cabinet(authorization):
    with allure.step('Открытие дропдауна в хедере'):
        main_page.header_drop_button()

    with allure.step('Клик по кнопке "Кабинет подкастера"'):
        main_page.to_cabinet_button()

    podcaster.close_monetization()