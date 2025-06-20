import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    def select_game(self, game_title):
        game_xpath = (By.XPATH, f"//p[@title='{game_title}']")
        self.click(game_xpath)
        self.wait_for_dom_and_network()

    def scroll_and_click_first_article(self):
        # Wait until at least one article is present
        self.get_element((By.XPATH, "//article"))

        # 🔄 Trigger lazy loading: scroll and wait twice
        for _ in range(2):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(0.5)  # slight buffer for scroll animation (optional)
            self.wait_for_dom_and_network()

        # Now click the first article
        self.click((By.XPATH, "//article"))
        self.wait_for_dom_and_network()
