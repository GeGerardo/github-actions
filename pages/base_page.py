from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

"""This class is parent of all pages"""
"""It contains all the generic methods and utilities"""


class BasePage:
    TARGET_URL = ""

    """Header Locators"""
    HEAD_CUSTOMER = (By.XPATH, "//a[text()='Our Customers ']")
    HEAD_PLATFORM = (By.XPATH, "//a[text()='Platform']")
    HEAD_LEARN = (By.XPATH, "//a[text()='Learn']")
    HEAD_COMPANY = (By.XPATH, "//a[text()='Company']")
    HEAD_SIGN = (By.XPATH, "//a[text()='Sign in']")

    """Footer Locators"""
    FOOTER_COMMUNITY = (By.XPATH, "//div[contains(@class,'footer-section')]"
                                  "//a[text()='Xeneta Customer Community']")
    FOOTER_PARTNER = (By.XPATH, "//div[contains(@class,'footer-section')]"
                                "//a[text()='Partner Directory']")
    FOOTER_COMPARE = (By.XPATH, "//div[contains(@class,'footer-section')]//a[text()='Compare Xeneta']")
    FOOTER_CAREERS = (By.XPATH, "//div[contains(@class,'footer-section')]//a[text()='Careers']")
    FOOTER_NEWS = (By.XPATH, "//div[contains(@class,'footer-section')]//a[text()='News']")
    FOOTER_CONTACT = (By.XPATH, "//div[contains(@class,'footer-section')]//a[text()='Contact Us']")
    FOOTER_PRESS = (By.XPATH, "//div[contains(@class,'footer-section')]//a[text()='Press Room']")
    FOOTER_XENETA = (By.XPATH, "//div[contains(@class,'footer-section')]//a[contains(@href,'xeneta')]")
    FOOTER_LINKEDIN = (By.XPATH, "//div[contains(@class,'footer-section')]//a[contains(@href,'linkedin')]")
    FOOTER_TWITTER = (By.XPATH, "//div[contains(@class,'footer-section')]//a[contains(@href,'twitter')]")
    FOOTER_YOUTUBE = (By.XPATH, "//div[contains(@class,'footer-section')]//a[contains(@href,'youtube')]")
    FOOTER_INSTAGRAM = (By.XPATH, "//div[contains(@class,'footer-section')]//a[contains(@href,'instagram')]")

    """Cookies Policy Locators"""
    COOKIES_BAR = (By.ID, "hs-eu-cookie-confirmation")
    COOKIES_ACCEPT = (By.ID, "hs-eu-confirmation-button")
    COOKIES_DECLINE = (By.ID, "hs-eu-decline-button")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.TARGET_URL)

    #######################################################################################
    '''Generic methods for re-use'''

    def do_click(self, by_locator, error='?'):
        WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(by_locator), message=' "%s"' % error).click()

    def do_dropdown_list(self, by_locator, option, error='?'):
        element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(by_locator), message=' "%s"' % error)
        select_dropdown = Select(element)
        select_dropdown.select_by_visible_text(option)

    def do_send_keys(self, by_locator, text, error='?'):
        WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(by_locator), message=' "%s"' % error).send_keys(text)

    def get_element_text(self, by_locator, error='?'):
        element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(by_locator), message=' "%s"' % error)
        return element.text

    def is_visible(self, by_locator, error='?'):
        element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(by_locator), message='Not visible: "%s"' % error)
        return bool(element)

    def is_not_visible(self, by_locator, error='?'):
        element = WebDriverWait(self.driver, 10) \
            .until(EC.invisibility_of_element_located(by_locator), message=' "%s"' % error)
        return bool(element)

    def get_link(self, url, error='?'):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url), message=' "%s"' % error)

    def count_elements(self, by_locator, error='?'):
        elements = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_all_elements_located(by_locator), message=' "%s"' % error)
        return elements

    def count_elements_not_visible(self, by_locator, error='?'):
        elements = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_all_elements_located(by_locator), message=' "%s"' % error)
        return elements

    def get_title(self, title, error='?'):
        WebDriverWait(self.driver, 10).until(EC.title_is(title), message=' "%s"' % error)
        return self.driver.title

    def go_back(self):
        self.driver.back()

    #######################################################################################
    '''Methods related to the header'''

    def is_header_customer_exist(self):
        return self.is_visible(self.HEAD_CUSTOMER, 'is_header_customer')

    def is_header_platform_exist(self):
        return self.is_visible(self.HEAD_PLATFORM, 'is_header_platform')

    def is_header_learn_exist(self):
        return self.is_visible(self.HEAD_LEARN, 'is_header_learn')

    def is_header_company_exist(self):
        return self.is_visible(self.HEAD_COMPANY, 'is_header_company')

    def is_header_sign_exist(self):
        return self.is_visible(self.HEAD_SIGN, 'is_header_sign')

    #######################################################################################
    '''Methods related to the footer'''

    def is_footer_community_exist(self):
        return self.is_visible(self.FOOTER_COMMUNITY, 'is_footer_community')

    def is_footer_partner_exist(self):
        return self.is_visible(self.FOOTER_PARTNER, 'is_footer_partner')

    def is_footer_compare_exist(self):
        return self.is_visible(self.FOOTER_COMPARE, 'is_footer_compare')

    def is_footer_careers_exist(self):
        return self.is_visible(self.FOOTER_CAREERS, 'is_footer_careers')

    def is_footer_news_exist(self):
        return self.is_visible(self.FOOTER_NEWS, 'is_footer_news')

    def is_footer_contact_exist(self):
        return self.is_visible(self.FOOTER_CONTACT, 'is_footer_contact')

    def is_footer_press_exist(self):
        return self.is_visible(self.FOOTER_PRESS, 'is_footer_press')

    def is_footer_xeneta_exist(self):
        return self.is_visible(self.FOOTER_XENETA, 'is_footer_xeneta')

    def is_footer_linkedin_exist(self):
        return self.is_visible(self.FOOTER_LINKEDIN, 'is_footer_linkedin')

    def is_footer_twitter_exist(self):
        return self.is_visible(self.FOOTER_TWITTER, 'is_footer_twitter')

    def is_footer_youtube_exist(self):
        return self.is_visible(self.FOOTER_YOUTUBE, 'is_footer_youtube')

    def is_footer_instagram_exist(self):
        return self.is_visible(self.FOOTER_INSTAGRAM, 'is_footer_instagram')

    #######################################################################################
    '''Methods related to Cookies Policy'''

    def is_cookies_bar_exist(self):
        return self.is_visible(self.COOKIES_BAR, 'is_cookies_bar')

    def accept_cookies(self):
        return self.do_click(self.COOKIES_ACCEPT, 'accept_cookies')

    def decline_cookies(self):
        return self.do_click(self.COOKIES_DECLINE, 'decline_cookies')

    def is_cookies_not_visible(self):
        return self.is_not_visible(self.COOKIES_BAR, 'is_cookies_not_visible')
