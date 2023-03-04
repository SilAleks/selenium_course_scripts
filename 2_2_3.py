from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    # класс для поиска по спискам
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # мой код
    
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    sum_num = str(int(num1) + int(num2))
    print("Summa ", sum_num, type(sum_num))
    
    # Кликаем
    browser.find_element(By.TAG_NAME, "select").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_num) # поиск эл-та списка с помощью класса Select
    #browser.find_element(By.CSS_SELECTOR, "[value=sum_num]").click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

