from selenium import webdriver


class Browser(object):
    driver = webdriver.Firefox()

    def quit(self):
        self.driver.quit()
