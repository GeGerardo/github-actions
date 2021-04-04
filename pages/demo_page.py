from selenium.webdriver.common.by import By
from config.config import TestData
from pages.base_page import BasePage


class DemoPage(BasePage):
    TARGET_URL = TestData.DEMO_URL

    """General Locators for the Demo page"""
    WATCH_BUTTON = (By.XPATH, "//span/a[text()='WATCH VIDEOS']")
    SCHEDULE_BUTTON = (By.XPATH, "//span/a[text()='Schedule Now']")
    SIGNUP_BUTTON = (By.XPATH, "//span/a[text()='Sign up here']")

    """Schedule Locators"""
    SCHEDULE_MODAL = (By.ID, "form-popup-2")
    SCHEDULE_CLOSE = (By.CSS_SELECTOR, ".close-modal")
    SCHEDULE_FIRSTNAME = (By.CSS_SELECTOR, "#form-popup-2 .hs_firstname input")
    SCHEDULE_LASTNAME = (By.CSS_SELECTOR, "#form-popup-2 .hs_lastname input")
    SCHEDULE_COMPANY = (By.CSS_SELECTOR, "#form-popup-2 .hs_company input")
    SCHEDULE_EMAIL = (By.CSS_SELECTOR, "#form-popup-2 .hs-email input")
    SCHEDULE_CHECKBOX_SUBSCRIBE = (By.CSS_SELECTOR, "#form-popup-2 "
                                                    ".hs_xeneta_industry_blog_instant_email_subscription input")
    SCHEDULE_CHECKBOX_AGREE = (By.CSS_SELECTOR, "#form-popup-2 .hs_confirm_opt_in input")
    SCHEDULE_CONFIRM = (By.CSS_SELECTOR, "#form-popup-2 .hs_submit input")
    SCHEDULE_PRIVACY_LINK = (By.CSS_SELECTOR, "#form-popup-2 .hs_email a")
    SCHEDULE_PRIVACY_LINK2 = (By.CSS_SELECTOR, "#form-popup-2 .hs-richtext.hs-main-font-element a")
    SCHEDULE_PRIVACY_LINK3 = (By.CSS_SELECTOR, "#form-popup-2 .hs_confirm_opt_in a")
    # SCHEDULE_PRIVACY_LINK2 = (By.CSS_SELECTOR, '#label-email-8c92c318-ab09-46db-a240-a2827276050d_762 a')

    """Sign UP Locators"""
    SIGNUP_MODAL = (By.ID, "form-popup-3")
    SIGNUP_CLOSE = (By.CSS_SELECTOR, ".close-modal")
    SIGNUP_FIRSTNAME = (By.CSS_SELECTOR, "#form-popup-3 .hs_firstname input")
    SIGNUP_LASTNAME = (By.CSS_SELECTOR, "#form-popup-3 .hs_lastname input")
    SIGNUP_COMPANY = (By.CSS_SELECTOR, "#form-popup-3 .hs_company input")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "#form-popup-3 .hs_email input")
    SIGNUP_JOB_TITLE = (By.CSS_SELECTOR, "#form-popup-3 .hs_jobtitle input")
    SIGNUP_DROPDOWN = (By.CSS_SELECTOR, "#form-popup-3 .hs_type_of_prospect select")
    SIGNUP_CHECKBOX_SUBSCRIBE = (By.CSS_SELECTOR, "#form-popup-3 "
                                                  ".hs_xeneta_industry_blog_instant_email_subscription input")
    SIGNUP_CHECKBOX_AGREE = (By.CSS_SELECTOR, "#form-popup-3 .hs_confirm_opt_in input")
    SIGNUP_CONFIRM = (By.CSS_SELECTOR, "#form-popup-3 .hs_submit input")
    SIGNUP_PRIVACY_LINK = (By.CSS_SELECTOR, "#form-popup-3 .hs_email a")
    SIGNUP_PRIVACY_LINK2 = (By.CSS_SELECTOR, "#form-popup-3 .hs-richtext.hs-main-font-element a")
    SIGNUP_PRIVACY_LINK3 = (By.CSS_SELECTOR, "#form-popup-3 .hs_confirm_opt_in a")
    # SIGNUP_CAPTCHA_BOX = (By.ID, 'rc-imageselect')

    #######################################################################################
    """Watch Videos related methods"""

    def click_watch_video(self):
        return self.do_click(self.WATCH_BUTTON, 'click_watch_video')

    def check_watch_video_page(self):
        return self.get_link(TestData.WATCH_VIDEO_URL, 'check_watch_video_page')

    #######################################################################################
    """Schedule Now related methods"""

    def click_schedule_now(self):
        return self.do_click(self.SCHEDULE_BUTTON, 'click_schedule_now')

    def check_schedule_modalbox(self):
        return self.is_visible(self.SCHEDULE_MODAL, 'check_schedule_modalbox')

    def close_schedule_modalbox(self):
        return self.do_click(self.SCHEDULE_CLOSE, 'close_schedule_modalbox')

    def is_schedule_not_visible(self):
        return self.is_not_visible(self.SCHEDULE_MODAL, 'is_schedule_not_visible')

    def click_schedule_privacy_link(self):
        return self.do_click(self.SCHEDULE_PRIVACY_LINK, 'click_schedule_privacy_link')

    def check_privacy_police_link(self):
        return self.get_link(TestData.PRIVACY_POLICY_URL, 'privacy_police_link')

    def fill_schedule_firstname(self):
        return self.do_send_keys(self.SCHEDULE_FIRSTNAME, TestData.FIRST_NAME, 'fill_schedule_firstname')

    def fill_schedule_lastname(self):
        return self.do_send_keys(self.SCHEDULE_LASTNAME, TestData.LAST_NAME, 'fill_schedule_lastname')

    def fill_schedule_companyname(self):
        return self.do_send_keys(self.SCHEDULE_COMPANY, TestData.COMPANY_NAME, 'fill_schedule_companyname')

    def fill_schedule_email(self):
        return self.do_send_keys(self.SCHEDULE_EMAIL, TestData.EMAIL, 'fill_schedule_email')

    def fill_schedule_subscribe(self):
        return self.do_click(self.SCHEDULE_CHECKBOX_SUBSCRIBE, 'fill_schedule_subscribe')

    def fill_schedule_agree(self):
        return self.do_click(self.SCHEDULE_CHECKBOX_AGREE, 'fill_schedule_agree')

    def fill_schedule_confirm(self):
        return self.do_click(self.SCHEDULE_CONFIRM, 'fill_schedule_confirm')

    # def check_captcha_box(self):
    #     return self.is_visible(self.SCHEDULE_CAPTCHA_BOX, 'check_captcha_box')

    #######################################################################################
    """SIGN UP related methods"""

    def click_signup(self):
        return self.do_click(self.SIGNUP_BUTTON, 'click_signup')

    def check_signup_modalbox(self):
        return self.is_visible(self.SIGNUP_MODAL, 'check_signup_modalbox')

    def close_signup_modalbox(self):
        return self.do_click(self.SIGNUP_CLOSE, 'close_signup_modalbox')

    def is_signup_not_visible(self):
        return self.is_not_visible(self.SIGNUP_MODAL, 'is_signup_not_visible')

    def fill_signup_firstname(self):
        return self.do_send_keys(self.SIGNUP_FIRSTNAME, TestData.FIRST_NAME, 'fill_signup_firstname')

    def fill_signup_lastname(self):
        return self.do_send_keys(self.SIGNUP_LASTNAME, TestData.LAST_NAME, 'fill_signup_lastname')

    def fill_signup_companyname(self):
        return self.do_send_keys(self.SIGNUP_COMPANY, TestData.COMPANY_NAME, 'fill_signup_companyname')

    def fill_signup_email(self):
        return self.do_send_keys(self.SIGNUP_EMAIL, TestData.EMAIL, 'fill_signup_email')

    def fill_signup_jobtitle(self):
        return self.do_send_keys(self.SIGNUP_JOB_TITLE, TestData.JOB_TITLE, 'fill_signup_jobtitle')

    def fill_signup_company_dropdown(self):
        self.do_dropdown_list(self.SIGNUP_DROPDOWN, TestData.COMPANY_TYPE_DROPDOWN, 'fill_signup_company_dropdown')

    def fill_signup_subscribe(self):
        return self.do_click(self.SIGNUP_CHECKBOX_SUBSCRIBE, 'fill_signup_subscribe')

    def fill_signup_agree(self):
        return self.do_click(self.SIGNUP_CHECKBOX_AGREE, 'fill_signup_agree')

    def fill_signup_confirm(self):
        return self.do_click(self.SIGNUP_CONFIRM, 'fill_signup_confirm')

    def check_signup_confirmation_page(self):
        return self.get_link(TestData.SIGNING_CONFIRMATION_URL, 'signup_confirmation_page')

    def click_signup_privacy_link(self):
        return self.do_click(self.SIGNUP_PRIVACY_LINK, 'click_signup_privacy_link')
