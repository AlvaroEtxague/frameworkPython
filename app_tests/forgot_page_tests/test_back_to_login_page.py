from pytest import mark
import allure


@mark.forgot_pass
@allure.description("A user can navigate back to the Login page")
@allure.severity(severity_level="NORMAL")
@mark.parametrize('my_browser', ['chrome', 'firefox'])
def test_success_forgot_password_page(forgot_pass, my_browser):
    try:
        forgot_pass.assert_back_to_login_page_link_text()
    finally:
        if AssertionError:
            allure.attach(forgot_pass.driver.get_screenshot_as_png(),
                          name="Back to login link",
                          attachment_type=allure.attachment_type.PNG)
    forgot_pass.click_back_to_login_link()
