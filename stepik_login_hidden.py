import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_login_stepik(browser):
    login = ""
    password = ""
    link = f"https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "ember503"), "Войти"))
    login_btn = browser.find_element(By.ID, "ember503")
    login_btn.click()

    WebDriverWait(browser, 15).until(EC.visibility_of(browser.find_element(By.ID, "id_login_email")))
    input_email = browser.find_element(By.ID, "id_login_email")
    input_email.send_keys(login)
    input_password = browser.find_element(By.ID, "id_login_password")
    input_password.send_keys(password)

    btn = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    btn.click()
    time.sleep(3)

    
