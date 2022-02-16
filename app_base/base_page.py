from selenium import webdriver


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def initial_setup(self, browser="chrome"):
        if browser.lower() == "chrome":
            try:
                self.options = webdriver.ChromeOptions()
                self.options.headless = True
                self.options.add_argument("start-maximized")
                self.options.add_experimental_option(
                    'excludeSwitches', ['enable-logging'])
                self.driver = webdriver.Chrome(
                    options=self.options)
                self.driver.implicitly_wait(10)
            except:
                raise Exception(
                    "Something is wrong. Couldn't start Chromedriver")

        elif browser.lower() == "firefox":
            try:
                self.options = webdriver.FirefoxOptions()
                self.options.headless = True
                self.options.add_argument("start-maximized")
                self.driver = webdriver.Firefox(
                    options=self.options)
                self.driver.implicitly_wait(10)
            except:
                raise Exception(
                    "Something is wrong. Couldn't start FirefoxDriver")

    def screenshot(self):
        self.driver.get_screenshot_as_png()
