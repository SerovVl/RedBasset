from selene import browser, have


class MainPage:

    def open(self, value):
        browser.open(value)

    def click_log_in_button(self):
        browser.element('[data-spec="header-auth-button"]').click()

    def shoud_authorized(self, value):
        browser.element('[data-spec="header-drop-button"]').should(have.text(value))

    def header_drop_button(self):
        browser.element('[data-spec="header-drop-button"]').click()

    def to_cabinet_button(self):
        browser.element('[data-spec="header-drop-item-1"]').click()
