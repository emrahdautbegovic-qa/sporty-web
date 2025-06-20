import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "Pixel 2"})
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
