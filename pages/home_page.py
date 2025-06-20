from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    BROWSE_BUTTON = (By.XPATH, "//div[contains(text(), 'Browse')]")
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")

    def open(self):
        self.driver.get("https://m.twitch.tv/")
        self.wait_for_title("Twitch")
        self.wait_for_dom_and_network()

    def click_browse(self):
        self.click(self.BROWSE_BUTTON)
        self.wait_for_dom_and_network()

    def search_game(self, game_name):
        self.enter_text(self.SEARCH_INPUT, game_name)
        self.wait_for_dom_and_network()
