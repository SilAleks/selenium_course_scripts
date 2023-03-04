from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    #browser.execute_script("document.title='Script для заголовока';")   # меняет заголовок страницы
    #browser.execute_script("alert('Robots at work');")             # вызвает alert в браузере
    # либо
    browser.execute_script("document.title='Script для заголовока';alert('Robots at work');")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
