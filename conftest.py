from pytest import fixture
from app_pages.primer_login import LoginPage
from app_pages.primer_forgot_password import ForgotPasswordPage
from app_base.base_page import BasePage as basepage


@fixture(scope='function')
def login_page():
    login_page = LoginPage(basepage)
    login_page.initial_setup()
    login_page.go()
    login_page.assert_login_page_url()
    login_page.assert_login_page_title()
    print("\n Initialize login page")
    return login_page


@fixture(scope='function')
def forgot_pass():
    forgot_pass_page = ForgotPasswordPage(basepage)
    forgot_pass_page.initial_setup()
    forgot_pass_page.go()
    forgot_pass_page.assert_forgot_password_page_url()
    forgot_pass_page.assert_forgot_password_page_title()
    print("\n Initialize forgot password page")
    return forgot_pass_page
