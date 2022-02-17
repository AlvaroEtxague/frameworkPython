from app_pages.primer_forgot_password import ForgotPasswordPage
from app_base.base_page import BasePage as basepage
from pytest import mark
import allure

@mark.forgot_pass
@allure.description("A user can submit a request to reset their password")
@allure.severity(severity_level="CRITICAL")
@mark.parametrize('my_browser', [('chrome'), ('firefox')])
def test_success_forgot_password_page(my_browser):
    email = "test@test.com"
    forgot_pass = ForgotPasswordPage(basepage)
    forgot_pass.initial_setup()
    forgot_pass.go()
    forgot_pass.assert_forgot_password_page_url()
    forgot_pass.assert_forgot_password_page_title()
    forgot_pass.input_email(email)
    forgot_pass.assert_back_to_login_page_link_text()
    forgot_pass.click_request_link_button()
    try:
        forgot_pass.assert_email_sent_msg(email)
    finally:
        if AssertionError:
            allure.attach(forgot_pass.driver.get_screenshot_as_png(),
                          name="Email sent message",
                          attachment_type=allure.attachment_type.PNG)
    forgot_pass.quit()
