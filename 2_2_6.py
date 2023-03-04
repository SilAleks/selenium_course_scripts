from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    # класс для поиска по спискам
import time
import math
from math import log, sin

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # мой код
    
    x = browser.find_element(By.ID, "input_value").text
    result = log(abs(12*sin(int(x))))
    #print(x, result) # проверка значений
    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(result) # вводим результат
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) # скроллит страницу, чтоб button стал видимым
    
    # Кликаем
    check_robot = browser.find_element(By.ID, "robotCheckbox")
    check_robot.click()
    radio_robot = browser.find_element(By.ID, "robotsRule")
    radio_robot.click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

