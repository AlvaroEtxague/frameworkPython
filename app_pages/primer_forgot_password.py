from selenium.webdriver.common.by import By
from app_base.base_page import BasePage as basepage
from app_base.base_element import BaseElement
from app_pages.primer_forgot_password_locators import ForgotPasswordPageLocators
from app_pages.locators.locator import Locator
from app_pages.login import LoginPage


class ForgotPasswordPage(basepage):
    url = "https://sandbox-dashboard.primer.io/forgot-password"

    @property
    def input_username(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=ForgotPasswordPageLocators.username)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def click_request_link_button(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=ForgotPasswordPageLocators.request_link_button)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def click_back_to_login_button(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=ForgotPasswordPageLocators.back_to_login_page_link)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_empty_email_input_validation(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=ForgotPasswordPageLocators.username_validation)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_email_sent_message(self):
        locator = Locator(by=By.CSS_SELECTOR,
                          value=ForgotPasswordPageLocators.email_sent_message)
        return BaseElement(driver=self.driver, locator=locator)


    def back_to_login(self):
        assert self.click_back_to_login_button.getText == "Login"
        self.click_back_to_login_button.click()
        assert LoginPage.click_login_button.getText == "Log in"
        assert LoginPage.click_forgot_password_button.getText == "Forgot password?"
