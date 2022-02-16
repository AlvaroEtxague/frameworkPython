from app_pages.login import LoginPage
from app_base.base_page import BasePage as basepage
from pytest import mark

@mark.login
@mark.parametrize('my_browser', [('chrome'),('firefox')])
class LoginTests:
    def test_login_page(self, my_browser):
        login_page = LoginPage(basepage)
        login_page.initial_setup(my_browser)
        login_page.go()
        assert login_page.click_login_button.getText == "Log in"
        login_page.page_login("good@email.com", "goodpass1")
        login_page.quit()

    def test_incorrect_email_login_error(self, my_browser):
        login_page = LoginPage(basepage)
        login_page.initial_setup(my_browser)
        login_page.go()
        assert login_page.click_login_button.getText == "Log in"
        login_page.page_login("bad@email.com", "goodpass1")
        assert login_page.get_credentials_error.getText == "Incorrect username or password"
        login_page.quit()

    def test_incorrect_password_login_error(self, my_browser):
        login_page = LoginPage(basepage)
        login_page.initial_setup(my_browser)
        login_page.go()
        assert login_page.click_login_button.getText == "Log in"
        login_page.page_login("good@email.com", "badpass1")
        assert login_page.get_credentials_error.getText == "Incorrect username or password"
        login_page.quit()
