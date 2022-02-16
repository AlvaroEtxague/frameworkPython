from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for all login page locators."""

    username = "input#username"
    password = "input#password"
    login_button = "form > .Button__ButtonRaw-sc-zydeuu-0.gdVDxr"
    incorrect_credentials = ".Text__Root-sc-1qalxlo-0.fDJYka"
    forgot_password_button = "[href='\/forgot-password']"
