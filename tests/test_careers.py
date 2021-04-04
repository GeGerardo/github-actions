import pytest
from pages.careers_page import CareersPage


# This fixture call the setup inside of conftest.py
@pytest.mark.usefixtures('setup')
class TestCareersPage:

    # Check if it is possible to accept Cookies.
    # No cookies check is made. I should implement getCookies()
    def test_accept_cookies(self):
        careers_page = CareersPage(self.driver)
        careers_page.is_cookies_bar_exist()
        careers_page.accept_cookies()
        careers_page.is_cookies_not_visible()

    # Check if it is possible to decline Cookies.
    # No cookies check is made. I should implement getCookies()
    def test_decline_cookies(self):
        careers_page = CareersPage(self.driver)
        careers_page.is_cookies_bar_exist()
        careers_page.decline_cookies()
        assert careers_page.is_cookies_not_visible()

    # Check if elements are visible in the header
    def test_header_elements_visible(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.is_header_customer_exist()
        careers_page.is_header_sign_exist()
        careers_page.is_header_learn_exist()
        careers_page.is_header_company_exist()
        careers_page.is_header_platform_exist()

    # Check if elements are visible in the footer
    def test_footer_elements_visible(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.is_footer_community_exist()
        careers_page.is_footer_partner_exist()
        careers_page.is_footer_compare_exist()
        careers_page.is_footer_careers_exist()
        careers_page.is_footer_news_exist()
        careers_page.is_footer_contact_exist()
        careers_page.is_footer_press_exist()
        careers_page.is_footer_xeneta_exist()
        careers_page.is_footer_linkedin_exist()
        careers_page.is_footer_twitter_exist()
        careers_page.is_footer_youtube_exist()
        careers_page.is_footer_instagram_exist()

    # Check the first tab and your respective content
    def test_tab_one(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.click_tab_one()
        careers_page.check_tab_one()
        assert careers_page.compare_info_tab_one()

    # Check the second tab and your respective content
    def test_tab_two(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.click_tab_two()
        careers_page.check_tab_two()
        assert careers_page.compare_info_tab_two()

    # Check the third tab and your respective content
    def test_tab_three(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.click_tab_three()
        careers_page.check_tab_three()
        assert careers_page.compare_info_tab_three()

    # Check the fourth tab and your respective content
    def test_tab_four(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.click_tab_four()
        careers_page.check_tab_four()
        assert careers_page.compare_info_tab_four()

    # Test the the card and url for Oslo
    def test_office_oslo(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.click_oslo_card()
        careers_page.check_oslo_url()
        careers_page.go_back()
        careers_page.click_oslo_button()
        careers_page.check_oslo_url()

    # Test the card and url for new_york
    def test_office_new_york(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.click_new_york_card()
        careers_page.check_new_york_url()
        careers_page.go_back()
        careers_page.click_new_york_button()
        careers_page.check_new_york_url()

    # Test the card and url for Hamburg
    def test_office_hamburg(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        careers_page.click_hamburg_card()
        careers_page.check_hamburg_url()
        careers_page.go_back()
        careers_page.click_hamburg_button()
        careers_page.check_hamburg_url()

    # Compare the total amount of Open Roles and related URLs
    # For this we can only test the total amount, because the links change times to time
    def test_total_amount_jobs(self):
        careers_page = CareersPage(self.driver)
        careers_page.accept_cookies()
        open_roles = len(careers_page.count_open_roles())
        url_roles = len(careers_page.count_url_roles())
        assert open_roles == url_roles
