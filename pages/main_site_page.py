from selene import browser, have


class MainPage:

    def open(self, value):
        browser.open(value)
        return self

    def click_log_in_button(self):
        browser.element('[data-spec="header-auth-button"]').click()
        return self

    def shoud_authorized(self, value):
        browser.element('[data-spec="header-drop-button"]').should(have.text(value))
        return self

    def header_drop_button(self):
        browser.element('[data-spec="header-drop-button"]').click()
        return self


    def to_cabinet_button(self):
        browser.element('[data-spec="header-drop-item-1"]').click()
        return self

    def logout(self):
        browser.element('[data-spec="header-drop-item-2"]').click()
        return self