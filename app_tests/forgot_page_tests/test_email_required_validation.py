from pytest import mark
import allure

@mark.forgot_pass
@allure.description("A validation is displayed when the email field is not entered")
@allure.severity(severity_level="NORMAL")
@mark.parametrize('my_browser', [('chrome'), ('firefox')])
def test_email_required_validation(forgot_pass, my_browser):
        forgot_pass.click_request_link_button()
        try:
            forgot_pass.assert_empty_email_input_validation()
        finally:
            if AssertionError:
                allure.attach(forgot_pass.driver.get_screenshot_as_png(),
                        name="Empty email validation",
                        attachment_type=allure.attachment_type.PNG)
        forgot_pass.quit()
