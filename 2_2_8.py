from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # мой код
    input_firstname = browser.find_element(By.NAME, "firstname")
    input_firstname.send_keys("Ivan")
    input_lastname = browser.find_element(By.NAME, "lastname")
    input_lastname.send_keys("Petrov")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("IPetrov@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input_file = browser.find_element(By.ID, "file")
    input_file.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

