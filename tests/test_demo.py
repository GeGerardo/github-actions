import pytest
from pages.demo_page import DemoPage


# This fixture call the setup inside of conftest.py
@pytest.mark.usefixtures('setup')
class TestDemoPage:

    # Check if it is possible to accept Cookies.
    # No cookies check is made. I should implement getCookies()
    def test_accept_cookies(self):
        demo_page = DemoPage(self.driver)
        demo_page.is_cookies_bar_exist()
        demo_page.accept_cookies()
        demo_page.is_cookies_not_visible()

    # Check if it is possible to decline Cookies.
    # No cookies check is made. I should implement getCookies()
    def test_decline_cookies(self):
        demo_page = DemoPage(self.driver)
        demo_page.is_cookies_bar_exist()
        demo_page.decline_cookies()
        demo_page.is_cookies_not_visible()

    # Check if elements are visible in the header
    def test_header_elements_visible(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        assert demo_page.is_header_customer_exist()
        assert demo_page.is_header_sign_exist()
        assert demo_page.is_header_learn_exist()
        assert demo_page.is_header_company_exist()
        assert demo_page.is_header_platform_exist()

    # Check if elements are visible in the footer
    def test_footer_elements_visible(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.is_footer_community_exist()
        demo_page.is_footer_partner_exist()
        demo_page.is_footer_compare_exist()
        demo_page.is_footer_careers_exist()
        demo_page.is_footer_news_exist()
        demo_page.is_footer_contact_exist()
        demo_page.is_footer_press_exist()
        demo_page.is_footer_xeneta_exist()
        demo_page.is_footer_linkedin_exist()
        demo_page.is_footer_twitter_exist()
        demo_page.is_footer_youtube_exist()
        demo_page.is_footer_instagram_exist()

    # Check if the Watch Video button works and if it is going to the correct page.
    # See note in the functional_checks.xls regarding the link
    def test_watch_videos(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.click_watch_video()
        demo_page.check_watch_video_page()

    # Check if the Schedule Now modal box appears and close as expected
    def test_schedule_modal_elements(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.click_schedule_now()
        demo_page.check_schedule_modalbox()
        demo_page.close_schedule_modalbox()
        demo_page.is_schedule_not_visible()

    # Check if the privacy link is the correct one
    def test_schedule_privacy_link(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.click_schedule_now()
        demo_page.click_schedule_privacy_link()
        demo_page.check_privacy_police_link()

    # Check if it is possible to fill the Schedule Now form.
    # No submission is made because of the CAPTCHA
    '''Another issue is related to the modal box ID. The locator ID seems to be dynamic.
    Sometimes it is form-popup-2 and other form-popup-1. Because of this this, the test should be manual or always has
    to have the locator updated accordingly, until we have a fixed ID '''
    def test_schedule_modal_fill_form(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.click_schedule_now()
        demo_page.check_schedule_modalbox()
        demo_page.fill_schedule_firstname()
        demo_page.fill_schedule_lastname()
        demo_page.fill_schedule_companyname()
        demo_page.fill_schedule_email()
        demo_page.fill_schedule_subscribe()
        demo_page.fill_schedule_agree()
        demo_page.fill_schedule_confirm()
        demo_page.close_schedule_modalbox()

    # Check if the Sign Up modal box appears and closes as expected
    def test_signup_modal_elements(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.click_signup()
        demo_page.check_signup_modalbox()
        demo_page.close_signup_modalbox()
        demo_page.is_signup_not_visible()

    def test_signup_privacy_link(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.click_signup()
        demo_page.check_signup_modalbox()
        demo_page.click_signup_privacy_link()
        demo_page.check_privacy_police_link()

    # Check if it is possible to fill the Schedule Now form.
    # Submission is made
    def test_signup_modal_fill_form(self):
        demo_page = DemoPage(self.driver)
        demo_page.accept_cookies()
        demo_page.click_signup()
        demo_page.check_signup_modalbox()
        demo_page.fill_signup_firstname()
        demo_page.fill_signup_lastname()
        demo_page.fill_signup_companyname()
        demo_page.fill_signup_email()
        demo_page.fill_signup_jobtitle()
        demo_page.fill_signup_company_dropdown()
        demo_page.fill_signup_subscribe()
        demo_page.fill_signup_agree()
        demo_page.fill_signup_confirm()
        demo_page.check_signup_confirmation_page()

