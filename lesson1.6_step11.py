from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def register(browser, url):
    """Заполняет форму регистрации и проверяет успешное сообщение."""
    browser.get(url)

    # Поля ввода: используем уникальные селекторы для первого блока
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Петров")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("ivan@example.com")

    # Отправка формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)  # Ожидание появления результата

    # Проверка текста об успешной регистрации
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!"


def test_registration1():
    """Тест для корректной страницы registration1.html."""
    browser = webdriver.Chrome()
    try:
        register(browser, "http://suninjuly.github.io/registration1.html")
        print("Тест на registration1.html пройден успешно.")
    finally:
        browser.quit()


def test_registration2():
    """Тест для страницы registration2.html, ожидается падение с NoSuchElementException."""
    browser = webdriver.Chrome()
    try:
        register(browser, "http://suninjuly.github.io/registration2.html")
        print("Ошибка: тест на registration2.html не упал, баг не обнаружен.")
    except NoSuchElementException as e:
        print(f"Тест на registration2.html упал с ожидаемой ошибкой: {type(e).__name__}")
    finally:
        browser.quit()


if __name__ == "__main__":
    test_registration1()
    test_registration2()
    