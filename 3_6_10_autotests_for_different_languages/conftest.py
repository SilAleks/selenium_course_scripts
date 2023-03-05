import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: 'es' or 'fr'",
                     choices=("es", "fr"))

@pytest.fixture(scope="function")
def browser(request):
    print("\nStart browser..")
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    browser.get(f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()
