from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class VideoPlayerPage(BasePage):
    VIDEO_ELEMENT = (By.TAG_NAME, "video")

    def is_video_playing(self):
        return self.driver.execute_script("""
            const video = document.querySelector('video');
            return !!(video && !video.paused && !video.ended && video.readyState >= 2);
        """)

    def wait_until_video_plays(self, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.is_video_playing(),
                message="Timed out waiting for video to start playing"
            )
        except TimeoutException:
            # Optionally take a screenshot or log details for debugging
            self.take_screenshot("video_not_playing.png")
            raise
