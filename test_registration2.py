from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration_form_1(self):
        link = "http://suninjuly.github.io/registration1.html"
    
        browser = webdriver.Chrome()
        browser.get(link)

        input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first[required]")
        input_first_name.send_keys("Ivan")
        
        input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second[required]")
        input_last_name.send_keys("Petrov")
        
        input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third[required]")
        input_email.send_keys("test@example.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Can't get welcome_text")
        

    def test_registration_form_2(self):
        link = "http://suninjuly.github.io/registration2.html"
    
        browser = webdriver.Chrome()
        browser.get(link)

        input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first[required]")
        input_first_name.send_keys("Ivan")
        
        input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second[required]")
        input_last_name.send_keys("Petrov")
        
        input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third[required]")
        input_email.send_keys("test@example.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Can't get welcome_text")


if __name__ == "__main__":
    unittest.main()
    