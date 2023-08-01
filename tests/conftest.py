import pytest
from selene import browser
import os
from pages.authentication_page import AuthPage
from pages.main_site_page import MainPage

main_page = MainPage()
auth_page = AuthPage()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://redbasset.tech/')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()