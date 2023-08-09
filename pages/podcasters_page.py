import os
from tests import paths
from selene import browser, have, be, command
import time

# import tests

class PodcasterPage():

    def close_monetization(self):
        browser.element('/html/body/div[4]/div/div/button').click()

    def click_creating_author(self):
        browser.element('[data-spec="podcaster-new-author"]').click()
        return self

    def upload_image(self, file):
        browser.element('input[type=file]').send_keys(paths.get_path_to_file(file))
        return self

    def fill_author_name(self, value):
        browser.element('[name="mainInfo.name"]').should(be.blank).type(value)
        return self

    def fill_author_description(self, value):
        browser.element('[data-spec="podcaster-author-new-desc"]').should(be.blank).type(value)
        return self

    def additional_about_author(self):
        browser.element('[data-spec="podcaster-author-new-progress-1"]').click()
        return self

    def fill_additional_email(self, value):
        browser.element('[name="additionalInfo.email"]').should(be.blank).type(value)
        return self

    def fill_additional_phone(self, value):
        browser.element('[name="additionalInfo.phone"]').should(be.blank).type(value)
        return self

    def submit_button(self):
        browser.element('[data-spec="podcaster-author-new-submit"]').click()
        return self

    def shoul_exist_author(self, value):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[1]/aside').should(have.text(value))
        return self

    # def main_author_page(self, value):
    #     browser.all('[data-spec^="podcaster-sidebar-author"]').element_by(have.exact_text(value)).click()

    def click_creating_podcast(self):
        browser.element('[data-spec="podcaster-author-podcast-new"]').click()
        return self

    def fill_podcast_name(self, value):
        browser.element('[name="mainInfo.name"]').should(be.blank).type(value)
        return self

    def fill_description_podcast(self, value):
        browser.element('[data-spec="podcaster-podcast-new-desc"]').should(be.blank).type(value)
        return self

    def upload_podcast_image(self, file):
        browser.element('[data-spec="podcaster-podcast-new-cover"]').send_keys(paths.get_path_to_file(file))
        return self

    def click_settings_podcast(self):
        browser.element('[data-spec="podcaster-podcast-new-progress-1"]').click()
        return self

    def click_additional_podcast(self):
        browser.element('[data-spec="podcaster-podcast-new-progress-2"]').click()
        return self

    def choose_category(self, category):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[2]/div/div[1]/div[1]/div/div').perform(
            command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(category)).click()
        return self

    def choose_subcategory(self, subcategory):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[2]/div/div[1]/div[2]/div/div').perform(
            command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(subcategory)).click()
        return self

    def add_category(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[2]/div/button').click()
        return self

    def choose_language(self, language):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[2]/div/div[4]/div/div').perform(
            command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(language)).click()

    def next_page(self):
        browser.element('[data-spec="podcaster-podcast-new-next"]').click()
        return self

    def subtit_creating_podcast(self):
        browser.element('[data-spec="podcaster-podcast-new-submit"]').click()
        return self

    def shoul_exist_podcast(self, value):
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/h5').should(
            have.text(value))
        return self

    def podcast_sidebar_button(self, name):
        browser.all('[data-spec^="podcaster-sidebar-podcast"]').element_by(
            have.exact_text(name)).click()
        return self

    def creating_episode_button(self):
        browser.element('[data-spec="podcaster-episode-new"]').click()
        return self

    def upload_episode(self, file):
        browser.element('[data-spec="podcaster-episode-new-file"]').send_keys(paths.get_path_to_file(file))
        return self

    def fill_episode_name(self, name):
        browser.element('[data-spec="podcaster-episode-new-name"]').type(name)
        return self

    def fill_episode_description(self, description):
        browser.element('[aria-describedby^="placeholder"]').type(description)
        return self

    def settings_button_tab(self):
        browser.element('[data-spec="podcaster-episode-new-progress-1"]').click()
        return self

    def season_number(self, number):
        browser.element('[data-spec="podcaster-episode-new-season"]').type(number)
        return self

    def episode_number(self, number):
        browser.element('[data-spec="podcaster-episode-new-episode"]').type(number)
        return self

    def episode_type(self, type):
        browser.all('[class^="Typography_podcaster"]').element_by(have.exact_text(type)).click()
        return self

    def obscene_language(self, language):
        browser.all('[class^="Typography_podcaster"]').element_by(have.exact_text(language)).click()
        return self

    def episode_delay(self, year):
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div/label/span').click()
        browser.element('[class^="react-datepicker__navigation-icon"]').click()
        browser.all(
            '[class^="react-datepicker__day"]').element_by(
            have.exact_text(year)).click()
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div[2]/div/div/div/div[4]/button[2]').click()
        return self

    def publish_episode(self):
        browser.element('[data-spec="episode-new-save-publish"]').click()
        return self

    def author_settings(self):
        browser.element('[data-spec="podcaster-author-tab-settings"]').click()

    def delete_author(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div/div[5]/div/button').click()
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div/div[5]/div/div/ul/li[2]/button').click()
        browser.element('/html/body/div[2]/div[3]/div/div/div/div/div/button[2]').click()
        time.sleep(10)