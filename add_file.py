from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Константин")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Константинопольский")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.com")

    input_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'add_file.py')
    input_file.send_keys(file_path)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
