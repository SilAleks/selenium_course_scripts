import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By # Для поиска по селекторам
from selenium.webdriver.support.wait import WebDriverWait # Для паузы
from selenium.webdriver.support import expected_conditions as EC # Для паузы, пока эл-т не найден

def test_links():
    f = open("links.txt", "r", encoding="utf8")
    links = [i for i in f]
    f.close()
    return links

links = test_links()

@pytest.mark.registration
@pytest.mark.parametrize('link', links)
def test_registration(browser, link): 
    print(link)
    browser.get(link)
    time.sleep(2)
    button_login = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ember-view.navbar__auth_login"))).click()
    time.sleep(2)
    input_login = browser.find_element(By.ID, "id_login_email").send_keys("silnyagin.av@mail.ru")
    #input_password = browser.find_element(By.ID, "id_login_password")
    #input_password.send_keys("xxx")
    time.sleep(3)
    button_sign_form = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()
    time.sleep(3)
    answer = str(math.log(int(time.time())))
    input_answer = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(answer)
    #input_answer.send_keys(answer)
    time.sleep(3)
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    time.sleep(3)
    #final_offer = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.By.CSS_SELECTOR, "p.smart-hints__hint"))).text
    final_offer = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    print(f"\n {final_offer} \n")
    f = open("final_offer.txt", "a", encoding="utf8")
    f.write(final_offer)
    f.close()
    time.sleep(3)
    assert final_offer == "Correct!", f"\n !!! Итог {final_offer} \n"
