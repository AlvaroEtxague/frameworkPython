from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find_by()

    def find_by(self):
        element = wait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return None

    def click(self):
        element = wait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def input_text(self, text):
        element = wait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator))
        element.clear()
        element.send_keys(text)
        return None

    def select_from_dropdown(self, dropdown, value):
        dd_element = Select(dropdown)
        dd_element.select_by_value(value)
        return None

    @property
    def get_text(self):
        text = self.web_element.text
        return text
