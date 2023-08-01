from selene import browser, be


class AuthPage:
    def fill_email(self, email):
        browser.element('//*[@id="__next"]/div[1]/main/div/div[2]/form/div[1]/div[1]/label/input').should(
            be.blank).type(email)

    def fill_password(self, password):
        browser.element('//*[@id="__next"]/div[1]/main/div/div[2]/form/div[1]/div[2]/label/input').should(
            be.blank).type(password)

    def click_auth_button(self):
        browser.element('[data-spec="auth-login-button"]').click()
