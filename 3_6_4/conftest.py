import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

# Фикстура для отрытия/закрытия браузера Chrome
@pytest.fixture(scope="function")
def browser():
    print("\n Запуск браузера")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(5)
    print("\n Закрываем браузер")
    browser.quit()

# Фикстура для расчета ответа
#@pytest.fixture(scope="session")
#def answer():
#    return str(math.log(int(time.time())))
