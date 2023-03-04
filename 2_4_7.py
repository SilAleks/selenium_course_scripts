from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
from math import log, sin

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # мой код
    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID,'price'), '$100'))
    book = browser.find_element(By.ID, "book")
    book.click()

    x = browser.find_element(By.ID, "input_value").text
    result = log(abs(12*sin(int(x))))
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(result)
    
    # Отправляем заполненную форму
    submit = browser.find_element(By.ID, "solve")
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

