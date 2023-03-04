from selenium import webdriver
#from selenium.webdriver.firefox.options import Options # для версии geckodriver 0.32.2

# для версии geckodriver 0.32.0
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

# для версии geckodriver 0.32.2
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#options = Options()
#options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
#driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe', options=options)

driver.get("https://stepik.org/lesson/25969/step/8")
