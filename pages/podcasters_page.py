import os
import time

from tests import paths
from selene import browser, have, be, command


# import tests

class PodcasterPage:

    def close_monetization(self):
        monetization = browser.element('/html/body/div[4]/div/div/button')
        if (monetization.wait_until(be.visible)):
            monetization.click()
        return self

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

    def main_author_page(self, value):
        browser.all('[data-spec^="podcaster-sidebar-author"]').element_by(have.exact_text(value)).click()
        return self

    def main_author_page_hiden(self):
        browser.element('[data-spec^="podcaster-sidebar-author"]').should(be.hidden)
        return self

    def click_creating_podcast(self):
        browser.element('[data-spec="podcaster-author-podcast-new"]').click()
        return self

    def button_creating_podcast_hidden(self):
        browser.element('[data-spec="podcaster-author-podcast-new"]').should(be.hidden)
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

    def date_episode_delay(self, date):
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div/label/span').click()
        browser.element('[class^="react-datepicker__navigation-icon"]').click()
        browser.all(
            '[class^="react-datepicker__day"]').element_by(
            have.exact_text(date)).click()
        # browser.element(
        #     '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div[2]/div/div/div/div[4]/button[2]').click()
        return self

    def time_episode_delay(self, hours, minutes):
        # browser.element(
        #     '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div/label/span').click()
        # browser.element('[class^="react-datepicker__navigation-icon"]').click()
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div[2]/div/div/div/div[3]/div[2]/div/div/input[1]').type(
            hours).click()
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div[2]/div/div/div/div[3]/div[2]/div/div/input[2]').type(
            minutes).click()
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div/div[4]/div[2]/div/div/div/div[4]/button[2]').click()
        return self

    def publish_episode(self):
        browser.element('[data-spec="episode-new-save-publish"]').click()
        return self

    def author_settings(self):
        browser.element('[data-spec="podcaster-author-tab-settings"]').click()
        return self

    def delete_author(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div/div[5]/div/button').click()
        time.sleep(1)
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div/div[5]/div/div/ul/li[2]/button').click()
        time.sleep(1)
        browser.element('/html/body/div[2]/div[3]/div/div/div/div/div/button[2]').click()

        return self

    def delete_author_hidden(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div/div[5]/div/button').click()
        time.sleep(1)
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div/div[5]/div/div/ul/li[2]/button').should(
            be.hidden)
        time.sleep(1)
        return self

    def redacting_author_hidden(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div/div[5]/div/button').should(
            be.hidden)
        time.sleep(1)
        return self

    def delete_podcast(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/ul/li/a/div[3]/button').click()
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/ul/li/a/div[3]/div/ul/li[6]/button').click()
        browser.element('/html/body/div[2]/div[3]/div/div/div/div/div/button[2]').click()
        return self

    def delete_podcast_hidden(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/ul/li/a/div[3]/button').click()
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/ul/li/a/div[3]/div/ul/li[6]/button').should(be.hidden)
        return self

    def import_button(self):
        browser.element('[data-spec="podcaster-author-podcast-import"]').click()
        return self

    def import_input(self, rss):
        browser.element('[data-spec="import-search-input"]').type(rss)
        return self

    def search_by_rss(self):
        browser.element('[data-spec="import-search-button"]').click()
        return self

    def start_import(self):
        browser.element('[data-spec="podcast-import-submit"]').click()
        time.sleep(7)
        return self

    def members_button(self):
        browser.element('[data-spec="podcaster-author-tab-members"]').click()
        return self

    def adding_member_button(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[1]/div/div[2]/div/button').click()
        return self

    def adding_member_button_hidden(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[1]/div/div[2]/div/button').should(
            be.hidden)
        return self

    def email_input_member(self, email):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/div[1]/label/input').type(email)
        return self

    def choose_role_member(self, role):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/div[2]/div').perform(
            command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(role)).click()
        return self

    def choose_role_member_hidden(self, role):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/div[2]/div').perform(
            command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(role)).should(be.hidden)
        return self

    def add_member(self):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/button[2]').click()
        return self

    def deleteting_member(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/section/ul/li[2]/div/button').click()
        return self

    def deleteting_member_button_disabled(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/section/ul/li[1]/div/button').should(
            be.disabled)
        return self

    def confirm_deleting_member(self):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/div[2]/button[2]').click()
        return self

    def button_active_menu_inside_episode(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/section/div[1]/div[3]/button').click()
        return self

    def button_unpublishing_inside_episode(self):
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/section/div[1]/div[3]/div/ul/li[2]/button').click()
        return self

    def button_publishing_inside_episode(self):
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/section/div[1]/div[3]/div/ul/li[1]/button').click()
        return self

    def episode_status_unpublished(self, value):
        browser.element('[class*="0OSun"]').should(have.exact_text(value))
        return self

    def button_deleting_episode_inside_episode(self):
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/section/div[1]/div[3]/div/ul/li[3]/button').click()
        return self

    def button_deleting_episode_inside_episode_hiden(self):
        browser.element(
            '//*[@id="__next"]/div[1]/div/div/main/div[2]/section/div[1]/div[3]/div/ul/li[3]/button').should(be.hidden)
        return self

    def button_confirm_deleting_episode(self):
        browser.element('/html/body/div[2]/div[3]/div/div/div/div/div/button[2]').click()
        return self

    def check_no_episodes(self, value):
        browser.all('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div[2]/div/text()[1]').element_by(
            have.exact_text(value))
        return self

    def button_save_draft(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div/div/div/button[1]').click()
        return self

    def button_to_statistik(self):
        browser.element('[data-spec="podcaster-author-tab-statistics"]').click()
        return self

    def check_on_statistick_page(self, value):
        browser.all('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[2]/div[2]/h4').element_by(
            have.exact_text(value))
        return self

    def podcast_members_button(self):
        browser.element('[data-spec="podcaster-podcast-tab-members"]').click()
        return self

    def button_adding_members_in_podcast(self):
        browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div[1]/div/div[2]/div/button').click()
        return self

    def podcast_email_input_member(self, email):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/div[1]/label/input').type(email)
        return self

    def choose_role_member_in_podcast(self, role):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/div[2]/div').perform(
            command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(role)).click()
        return self

    def add_member_in_podcast(self):
        browser.element('/html/body/div[2]/div[3]/div/div/div/form/button[2]').click()
        return self

    def get_in_episode(self):
        browser.element('[class^="EpisodeCard_container"]').click()
        return self


