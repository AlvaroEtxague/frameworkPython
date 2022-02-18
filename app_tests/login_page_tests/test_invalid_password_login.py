from pytest import mark
import allure


@mark.login
@allure.description("A user with invalid password cannot login to Primer page")
@allure.severity(severity_level="CRITICAL")
@mark.parametrize('my_browser', [('chrome'), ('firefox')])
def test_invalid_password_login_error(login_page, my_browser):
    try:
        login_page.assert_login_btn_text()
    finally:
        if AssertionError:
            allure.attach(login_page.driver.get_screenshot_as_png(),
                          name="Login Page",
                          attachment_type=allure.attachment_type.PNG)
    login_page.login_to_primer("good@email.com", "badpass1")
    try:
        login_page.assert_invalid_credentials_validation()
    finally:
        if AssertionError:
            allure.attach(login_page.driver.get_screenshot_as_png(),
                          name="Invalid credentials validation",
                          attachment_type=allure.attachment_type.PNG)
    login_page.quit()
