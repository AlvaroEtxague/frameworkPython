# from app_pages.primer_forgot_password import ForgotPasswordPage
# from app_base.base_page import BasePage as basepage
# from pytest import mark
#
# @mark.forgot_pass
# class ForgotPasswordTests:
#     def test_success_forgot_password_page(self):
#         forgot_pass_page = ForgotPasswordPage(basepage)
#         forgot_pass_page.initial_setup()
#         forgot_pass_page.go()
#         forgot_pass_page.input_username.inputText("test@test.com")
#         assert forgot_pass_page.click_request_link_button.getText == "Request link"
#         forgot_pass_page.click_request_link_button.click()
#         assert forgot_pass_page.get_email_sent_message.getText == "An email has been sent to test@test.com with further instructions."
#         forgot_pass_page.quit()
#
#     def test_back_to_login_page(self):
#         forgot_pass_page = ForgotPasswordPage(basepage)
#         forgot_pass_page.initial_setup()
#         forgot_pass_page.go()
#         assert forgot_pass_page.click_request_link_button.getText == "Request link"
#         forgot_pass_page.click_back_to_login_button.click()
#         forgot_pass_page.quit()
#
#     def test_email_required_validation(self):
#         forgot_pass_page = ForgotPasswordPage(basepage)
#         forgot_pass_page.initial_setup()
#         forgot_pass_page.go()
#         assert forgot_pass_page.click_request_link_button.getText == "Request link"
#         forgot_pass_page.click_request_link_button.click()
#         assert forgot_pass_page.get_empty_email_input_validation.getText == "An email address is required"
#         forgot_pass_page.quit()
