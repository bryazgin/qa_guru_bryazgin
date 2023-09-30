import pytest
from selene import browser, be, have


@pytest.fixture()
def open_browser(browser_size):
    browser.open('https://google.com')


@pytest.fixture()
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_have_text(open_browser, browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_no_result_query(open_browser, browser_size):
    browser.element('[name="q"]').type('bhbhbbhbhbhbhbhhbbhbhbhb').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
