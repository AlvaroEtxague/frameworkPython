from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators(object):
    """A class for all login page locators."""
    url = "https://sandbox-dashboard.primer.io/forgot-password"
    forgot_password_title = ".Title__Root-sc-2rwlde-0.daVCtm"
    username = "input#username"
    username_validation = ".Text__Root-sc-1qalxlo-0.fDJYka"
    back_to_login_page_link = ".Link__StyledText-sc-1yxsw2a-0.Text__Root-sc-1qalxlo-0.dTwHUV.gOnIHd > span"
    request_link_button = ".Button__ButtonRaw-sc-zydeuu-0.gdVDxr > span"
    email_sent_message = ".Callout__ContentRoot-sc-d1p987-0.hRBCwa"
