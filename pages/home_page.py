from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class HomePage(BasePage):
    BROWSE_BUTTON = (By.XPATH, "//div[contains(text(), 'Browse')]")
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")

    def open(self):
        self.driver.get("https://m.twitch.tv/")
        self.wait_for_title("Twitch")
        self.wait_for_dom_and_network()
        self.dismiss_consent_banner()

    def click_browse(self):
        self.click(self.BROWSE_BUTTON)
        self.wait_for_dom_and_network()
       
    def search_game(self, game_name):
        self.enter_text(self.SEARCH_INPUT, game_name)
        self.wait_for_dom_and_network()
    
    def dismiss_consent_banner(self, timeout=5):
        consent_banner_locator = (By.CLASS_NAME, "consent-banner")
        button_locator = (
            By.XPATH,
            "//div[contains(@class,'consent-banner')]//button[" +
            "contains(text(), 'Accept') or contains(text(), 'Got it') or contains(text(), 'Dismiss') or contains(text(), 'Proceed') or contains(text(), 'Continue')"
            + "]"
        )
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*consent_banner_locator).is_displayed()
            )
            button = self.driver.find_element(*button_locator)
            if button.is_displayed() and button.is_enabled():
                button.click()
                self.wait_for_dom_and_network()
        except (TimeoutException, NoSuchElementException):
            pass
