from selenium.webdriver.common.by import By
from browser import Browser


class HomePageLocator(object):
    HEADER_TEXT = (By.XPATH, "/h1")
    SEARCH_FIELD = (By.ID, "search")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='content']/div[1]/div/form/button")


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)