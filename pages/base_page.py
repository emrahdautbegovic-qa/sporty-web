import time
import os
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    SCREENSHOTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'screenshots'))

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
        except Exception as e:
            self.take_screenshot("click_exception")
            raise e

    def enter_text(self, by_locator, text):
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.take_screenshot("enter_text_exception")
            raise e

    def wait_for_title(self, title_fragment):
        try:
            self.wait.until(EC.title_contains(title_fragment))
        except Exception as e:
            self.take_screenshot("wait_for_title_exception")
            raise e

    def get_element(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def setup_network_tracker(self):
        self.driver.execute_script("""
            window.__pendingXHR = 0;
            (function(open, send) {
                XMLHttpRequest.prototype.open = function() {
                    this.addEventListener('readystatechange', function() {
                        if (this.readyState === 1) window.__pendingXHR++;
                        if (this.readyState === 4) window.__pendingXHR--;
                    }, false);
                    open.apply(this, arguments);
                };
            })(XMLHttpRequest.prototype.open, XMLHttpRequest.prototype.send);

            window.__pendingFetch = 0;
            const originalFetch = window.fetch;
            window.fetch = function() {
                window.__pendingFetch++;
                return originalFetch.apply(this, arguments)
                    .finally(() => window.__pendingFetch--);
            };
        """)

    def wait_for_network_idle(self, timeout=15, idle_time=0.5, check_interval=0.2):
        start_time = time.time()
        last_active_time = time.time()

        while time.time() - start_time < timeout:
            active_requests = self.driver.execute_script("""
                return (window.__pendingXHR || 0) + (window.__pendingFetch || 0);
            """)
            if active_requests == 0:
                if time.time() - last_active_time >= idle_time:
                    return True
            else:
                last_active_time = time.time()
            time.sleep(check_interval)

        raise TimeoutError("Timed out waiting for network to become idle")

    def wait_for_dom_loaded(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") in ["interactive", "complete"]
            )
        except Exception as e:
            self.take_screenshot("wait_for_dom_loaded_exception")
            raise e

    def wait_for_dom_and_network(self):
        self.wait_for_dom_loaded()
        self.wait_for_network_idle()

    def take_screenshot(self, name_prefix="screenshot"):
        os.makedirs(self.SCREENSHOTS_PATH, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name_prefix}_{timestamp}.png"
        path = os.path.join(self.SCREENSHOTS_PATH, filename)
        self.driver.save_screenshot(path)
