from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # мой код
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    answer_x = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer_x)

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

