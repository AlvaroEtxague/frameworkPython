from selenium.webdriver.common.by import By
from app_base.base_page import BasePage as basepage
from app_base.base_element import BaseElement
import allure


class LoginPage(basepage):
    url = "https://sandbox-dashboard.primer.io/login"
    page_title = "Dashboard | Primer"

    # CONSTRUCTOR
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    username = (By.CSS_SELECTOR, "input#username")
    password = (By.CSS_SELECTOR, "input#password")
    login_button = (
    By.CSS_SELECTOR, "form > .Button__ButtonRaw-sc-zydeuu-0.gdVDxr")
    invalid_credentials = (By.CSS_SELECTOR, ".Text__Root-sc-1qalxlo-0.fDJYka")
    forgot_password_button = (By.CSS_SELECTOR, "[href*='/forgot-password']")

    # GETTERS
    @property
    def get_username_input(self):
        return BaseElement(driver=self.driver, locator=self.username)

    @property
    def get_password_input(self):
        return BaseElement(driver=self.driver, locator=self.password)

    @property
    def get_login_btn(self):
        return BaseElement(driver=self.driver, locator=self.login_button)

    @property
    def get_invalid_credentials_validation(self):
        return BaseElement(driver=self.driver,
                           locator=self.invalid_credentials)

    @property
    def get_forgot_pass_btn(self):
        return BaseElement(driver=self.driver,
                           locator=self.forgot_password_button)

    # PAGE ACTIONS
    @allure.step("Completing username in Login Page")
    def input_username(self, username):
        self.get_username_input.inputText(username)

    @allure.step("Completing password in Login Page")
    def input_password(self, password):
        self.get_password_input.inputText(password)

    @allure.step("Clicking Login button")
    def click_login_btn(self):
        self.get_login_btn.click()

    @allure.step("Asserting Login button text")
    def assert_login_btn_text(self):
        assert self.get_login_btn.getText == "Log in"

    @allure.step("Clicking Forgot Password button")
    def click_forgot_password_btn(self):
        self.get_forgot_pass_btn.click()

    @allure.step("Asserting Forgot Password button text")
    def assert_forgot_password_btn_text(self):
        assert self.get_forgot_pass_btn.getText == "Forgot password?"

    @allure.step("Asserting invalid credentials validation")
    def assert_invalid_credentials_validation(self):
        assert self.get_invalid_credentials_validation.getText == "Incorrect username or password"

    @allure.step("Asserting Login page url")
    def assert_login_page_url(self):
        assert self.get_page_url == self.url

    @allure.step("Asserting Login page title")
    def assert_login_page_title(self):
        assert self.get_page_title == self.page_title

    @allure.step("Log in to Primer")
    def login_to_primer(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()
