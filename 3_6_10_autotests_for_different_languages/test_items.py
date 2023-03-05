from selenium.webdriver.common.by import By # Для поиска по селекторам
import time

def test_btn_add_to_basket(browser):
    time.sleep(15)
    btn_add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "\n Нема кнопки !"
