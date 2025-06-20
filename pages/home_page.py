from selenium.webdriver.common.by import By
from pages.base_page import BasePage

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
    
    def dismiss_consent_banner(self):
        try:
            banner = self.driver.find_element(By.CLASS_NAME, "consent-banner")
            button = banner.find_element(By.XPATH, ".//button[contains(text(), 'Accept') or contains(text(), 'Got it') or contains(text(), 'Dismiss')]")
            if button.is_displayed():
                button.click()
                self.wait_for_dom_and_network()
        except Exception:
            # Banner may not exist — ignore safely
            pass
