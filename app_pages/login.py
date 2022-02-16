from selenium.webdriver.common.by import By
from app_base.base_page import BasePage as basepage
from app_base.base_element import BaseElement
from app_pages.login_locators import LoginPageLocators
from app_pages.locators.locator import Locator

class LoginPage(basepage):

    url = "https://sandbox-dashboard.primer.io/login"
    # url = "/login"

    @property
    def input_username(self):
        locator = Locator(by=By.CSS_SELECTOR, value=LoginPageLocators.username)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def input_password(self):
        locator = Locator(by=By.CSS_SELECTOR, value=LoginPageLocators.password)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def click_login_button(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=LoginPageLocators.login_button)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def click_forgot_password_button(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=LoginPageLocators.forgot_password_button)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_credentials_error(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=LoginPageLocators.incorrect_credentials)
        return BaseElement(driver=self.driver, locator=locator)

    def page_login(self, username, passwd):
        self.input_username.inputText(username)
        self.input_password.inputText(passwd)
        self.click_login_button.click()
