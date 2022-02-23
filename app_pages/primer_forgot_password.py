from selenium.webdriver.common.by import By
from app_base.base_page import BasePage as basepage
from app_base.base_element import BaseElement
from app_pages.primer_login import LoginPage
import allure


class ForgotPasswordPage(basepage):
    # CONSTRUCTOR
    def __init__(self, driver, conf):
        super().__init__(driver, conf)
        self.url = conf.env['forgot_pass_url']

    # LOCATORS
    forgot_password_title = (
        By.CSS_SELECTOR, ".Title__Root-sc-2rwlde-0.daVCtm")
    email = (By.CSS_SELECTOR, "input#username")
    email_validation = (By.CSS_SELECTOR, ".Text__Root-sc-1qalxlo-0.fDJYka")
    back_to_login_page_link = (By.CSS_SELECTOR,
                               ".Link__StyledText-sc-1yxsw2a-0.Text__Root-sc-1qalxlo-0.dTwHUV.gOnIHd > span")
    request_link_button = (
        By.CSS_SELECTOR, ".Button__ButtonRaw-sc-zydeuu-0.gdVDxr > span")
    email_sent_message = (
        By.CSS_SELECTOR, ".Callout__ContentRoot-sc-d1p987-0.hRBCwa")
    bad_request_message = (By.CSS_SELECTOR, ".Text__Root-sc-1qalxlo-0.fDJYka")

    # GETTERS
    @property
    def get_email_input(self):
        return BaseElement(driver=self.driver, locator=self.email)

    @property
    def get_email_address_validation(self):
        return BaseElement(driver=self.driver, locator=self.email_validation)

    @property
    def get_back_to_login_page_link(self):
        return BaseElement(
            driver=self.driver,
            locator=self.back_to_login_page_link
        )

    @property
    def get_request_link_btn(self):
        return BaseElement(
            driver=self.driver,
            locator=self.request_link_button
        )

    @property
    def get_email_sent_msg(self):
        return BaseElement(driver=self.driver, locator=self.email_sent_message)

    @property
    def get_forgot_password_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.forgot_password_title
        )

    @property
    def get_bad_request_validation(self):
        return BaseElement(
            driver=self.driver,
            locator=self.bad_request_message
        )

    # PAGE ACTIONS
    @allure.step("Completing username in Forgot Password Page")
    def input_email(self, email):
        self.get_email_input.input_text(email)

    @allure.step("Clicking Request Link button")
    def click_request_link_button(self):
        self.get_request_link_btn.click()

    @allure.step("Asserting Request Link button text")
    def assert_back_to_login_page_link_text(self):
        assert self.get_request_link_btn.get_text == "Request link"

    @allure.step("Clicking back to Login page Link")
    def click_back_to_login_link(self):
        self.get_back_to_login_page_link.click()

    @allure.step("Asserting empty email address validation")
    def assert_empty_email_input_validation(self):
        assert self.get_email_address_validation.get_text == "An email address is required"

    @allure.step("Asserting email sent message")
    def assert_email_sent_msg(self, email):
        assert self.get_email_sent_msg.get_text == "An email has been sent to " + \
            email + " with further instructions."

    @allure.step("Asserting bad request validation")
    def assert_bad_request_validation(self):
        assert self.get_bad_request_validation.get_text == "Something went wrong, please try again"

    @allure.step("Asserting Login button text")
    def assert_back_to_login_page_link_text(self):
        assert self.get_back_to_login_page_link.get_text == "Login"

    @allure.step("Asserting that we are back to Login Page")
    def back_to_login(self):
        self.assert_back_to_login_page_link_text()
        self.click_back_to_login_link()
        LoginPage.assert_login_page_url()
        LoginPage.assert_login_page_title()
        LoginPage.assert_login_btn_text()
        LoginPage.assert_forgot_password_btn_text()

    @allure.step("Asserting Forgot Password page url")
    def assert_forgot_password_page_url(self):
        assert self.get_page_url == self.url

    @allure.step("Asserting Forgot Password page title")
    def assert_forgot_password_page_title(self):
        assert self.get_page_title == self.page_title
