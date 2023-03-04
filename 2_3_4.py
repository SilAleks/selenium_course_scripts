from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from math import log, sin

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # мой код
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)
    x = browser.find_element(By.ID, "input_value").text
    result = log(abs(12*sin(int(x))))
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(result)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

