from config import Config
from pytest import fixture
from app_pages.primer_login import LoginPage
from app_pages.primer_forgot_password import ForgotPasswordPage
from app_base.base_page import BasePage as basepage


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        help='Environment to run tests'
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@fixture(scope='session')
def app_config(env):
    my_app_config = Config(env)
    return my_app_config


@fixture(scope='function')
def login_page(app_config):
    login_page = LoginPage(basepage, app_config)
    login_page.initial_setup()
    login_page.go()
    login_page.assert_login_page_url()
    login_page.assert_login_page_title()
    print("\n Initialize login page")
    yield login_page

    login_page.quit()


@fixture(scope='function')
def forgot_pass(app_config):
    forgot_pass_page = ForgotPasswordPage(basepage, app_config)
    forgot_pass_page.initial_setup()
    forgot_pass_page.go()
    forgot_pass_page.assert_forgot_password_page_url()
    forgot_pass_page.assert_forgot_password_page_title()
    print("\n Initialize forgot password page")
    yield forgot_pass_page

    forgot_pass_page.quit()
