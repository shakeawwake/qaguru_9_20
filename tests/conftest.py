import pytest

from selene import browser

LOGIN = "di7051@gmail.com"
PASSWORD = "T9tBaN!jx$XqC"
BASE_URL = "https://demowebshop.tricentis.com/"


@pytest.fixture()
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(BASE_URL)
    yield browser
    browser.quit()
