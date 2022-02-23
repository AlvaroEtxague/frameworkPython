from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure


class BasePage(object):

    def __init__(self, driver, conf):
        self.driver = driver
        self.url = conf.env['base_url']
        self.page_title = conf.env['page_title']
        self.env = conf.env

    @allure.step("Navigating to page")
    def go(self):
        self.driver.get(self.url)

    @allure.step("Closing page")
    def quit(self):
        self.driver.quit()

    @allure.step("Opening browser")
    def initial_setup(self, browser="chrome"):
        if browser.lower() == "chrome":
            try:
                serv = Service("resources/chromedriver.exe")
                self.options = webdriver.ChromeOptions()
                self.options.headless = True
                self.options.add_argument("start-maximized")
                self.options.add_experimental_option(
                    'excludeSwitches', ['enable-logging'])
                self.driver = webdriver.Chrome(
                    service=serv,
                    options=self.options)
                self.driver.implicitly_wait(10)
            except:
                raise Exception(
                    "Something is wrong. Couldn't start Chromedriver")

        elif browser.lower() == "firefox":
            try:
                serv = Service("resources/geckodriver.exe")
                self.options = webdriver.FirefoxOptions()
                self.options.headless = True
                self.options.add_argument("start-maximized")
                self.driver = webdriver.Firefox(
                    service=serv,
                    options=self.options)
                self.driver.implicitly_wait(10)
            except:
                raise Exception(
                    "Something is wrong. Couldn't start FirefoxDriver")

    @property
    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title

    @property
    @allure.step("Getting current URL of the page")
    def get_page_url(self):
        return self.driver.current_url

    def screenshot(self):
        self.driver.get_screenshot_as_png()
