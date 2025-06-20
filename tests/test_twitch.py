import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.video_player_page import VideoPlayerPage
from facade.steps import step


def test_mobile_twitch_flow(driver):
    home = HomePage(driver)
    search = SearchResultsPage(driver)
    player = VideoPlayerPage(driver)

    home.open()
    home.setup_network_tracker()
    step(home.click_browse, "Browse button not found")
    step(lambda: home.search_game("StarCraft II"), "Search input not found")
    step(lambda: search.select_game("StarCraft II"), "Game not found in search results")
    step(search.scroll_and_click_first_article, "Article not clickable")
    player.wait_until_video_plays()
    player.take_screenshot("player_loaded.png")