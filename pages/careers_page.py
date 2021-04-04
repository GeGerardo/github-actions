from selenium.webdriver.common.by import By
from config.config import TestData
from pages.base_page import BasePage


class CareersPage(BasePage):
    TARGET_URL = TestData.CAREERS_URL

    """General Locators for the Careers page"""
    TAB_ONE = (By.XPATH, "//li[@data-tab='Xenetaisone-1']")
    TAB_TWO = (By.XPATH, "//li[@data-tab='Modernizationthroughdata-2']")
    TAB_THREE = (By.XPATH, "//li[@data-tab='VarietyandFairness-3']")
    TAB_FOUR = (By.XPATH, "//li[@data-tab='TransparencybuildsTrust-4']")

    BOX_ONE = (By.CSS_SELECTOR, "#Xenetaisone-1 h2")
    BOX_TWO = (By.CSS_SELECTOR, "#Modernizationthroughdata-2 h2")
    BOX_THREE = (By.CSS_SELECTOR, "#VarietyandFairness-3 h2")
    BOX_FOUR = (By.CSS_SELECTOR, "#TransparencybuildsTrust-4 h2")

    CARD_OSLO = (By.CSS_SELECTOR, "#slick-slide00 .card-image.section-bg")
    CARD_NEW_YORK = (By.CSS_SELECTOR, "#slick-slide01 .card-image.section-bg")
    CARD_HAMBURG = (By.CSS_SELECTOR, "#slick-slide02 .card-image.section-bg")
    BUTTON_OSLO = (By.XPATH, "//a[contains(@href,'oslo') and @class='cta_button']")
    BUTTON_NEW_YORK = (By.XPATH, "//a[contains(@href,'new-york') and @class='cta_button']")
    BUTTON_HAMBURG = (By.XPATH, "//a[contains(@href,'hamburg') and @class='cta_button']")

    JOBS_URL_COUNT = (By.CSS_SELECTOR, ".subscription-model-inner a")
    JOBS_ROLES_COUNT = (By.CSS_SELECTOR, ".accordion_group")

    #######################################################################################
    """Tab one related methods"""

    # .lower() is used to avoid letter case issue
    # in is used to avoid empty space

    def click_tab_one(self):
        return self.do_click(self.TAB_ONE, 'click_tab_one')

    def check_tab_one(self):
        return self.is_visible(self.BOX_ONE, 'check_tab_one')

    def compare_info_tab_one(self):
        tab = self.get_element_text(self.TAB_ONE)
        box = self.get_element_text(self.BOX_ONE)
        return tab.lower() in box.lower()

    #######################################################################################
    """Tab two related methods"""

    # .lower() is used to avoid letter case issue
    # in is used to avoid empty space

    def click_tab_two(self):
        return self.do_click(self.TAB_TWO, 'click_tab_two')

    def check_tab_two(self):
        return self.is_visible(self.BOX_TWO, 'check_tab_two')

    def compare_info_tab_two(self):
        tab = self.get_element_text(self.TAB_TWO, 'get_element_tab')
        box = self.get_element_text(self.BOX_TWO, 'get_element_box')
        return tab.lower() in box.lower()

    #######################################################################################
    """Tab three related methods"""

    # .lower() is used to avoid letter case issue
    # in is used to avoid empty space

    def click_tab_three(self):
        return self.do_click(self.TAB_THREE, 'click_tab_three')

    def check_tab_three(self):
        return self.is_visible(self.BOX_THREE, 'check_tab_three')

    def compare_info_tab_three(self):
        tab = self.get_element_text(self.TAB_THREE, 'get_element_tab')
        box = self.get_element_text(self.BOX_THREE, 'get_element_box')
        return tab.lower() in box.lower()

    #######################################################################################
    """Tab four related methods"""

    # .lower() is used to avoid letter case issue
    # in is used to avoid empty space

    def click_tab_four(self):
        return self.do_click(self.TAB_FOUR, 'click_tab_four')

    def check_tab_four(self):
        return self.is_visible(self.BOX_FOUR, 'check_tab_four')

    def compare_info_tab_four(self):
        tab = self.get_element_text(self.TAB_FOUR, 'get_element_tab')
        box = self.get_element_text(self.BOX_FOUR, 'get_element_box')
        return tab.lower() in box.lower()

    #######################################################################################
    """Xeneta Offices related methods"""

    # Oslo Office
    def click_oslo_card(self):
        return self.do_click(self.CARD_OSLO, 'click_card_oslo')

    def check_oslo_url(self):
        return self.get_link(TestData.OSLO_URL, 'check_oslo_url')

    def click_oslo_button(self):
        return self.do_click(self.BUTTON_OSLO, 'click_oslo_button')

    # New York Office
    def click_new_york_card(self):
        return self.do_click(self.CARD_NEW_YORK, 'click_card_new_york')

    def check_new_york_url(self):
        return self.get_link(TestData.NEW_YORK_URL, 'check_new_york_url')

    def click_new_york_button(self):
        return self.do_click(self.BUTTON_NEW_YORK, 'click_new_york_button')

    # Hamburg Office
    def click_hamburg_card(self):
        return self.do_click(self.CARD_HAMBURG, 'click_card_hamburg')

    def check_hamburg_url(self):
        return self.get_link(TestData.HAMBURG_URL, 'check_hamburg_url')

    def click_hamburg_button(self):
        return self.do_click(self.BUTTON_HAMBURG, 'click_hamburg_button')

    #######################################################################################
    """Open Roles Card"""
    def count_open_roles(self):
        return self.count_elements_not_visible(self.JOBS_ROLES_COUNT, 'count_open_roles')

    def count_url_roles(self):
        return self.count_elements_not_visible(self.JOBS_URL_COUNT, 'count_url_roles')

