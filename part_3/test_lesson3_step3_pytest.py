from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def test_reg_form1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.XPATH, "// input[ @ placeholder = 'Input your first name']")
        first_name.send_keys("Мой ответ")
        last_name = browser.find_element(By.XPATH, "// input[ @ placeholder = 'Input your last name']")
        last_name.send_keys("Мой ответ")
        email = browser.find_element(By.XPATH, "// input[ @ placeholder = 'Input your email']")
        email.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual_welcome_text = welcome_text_elt.text
        # ожидаемый текст приветствия
        expected_welcome_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # self.assertEqual('что должно быть', 'что есть', 'что произошло')
        assert expected_welcome_text == actual_welcome_text, 'You doing something wrong'  # add assertion here

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_reg_form2():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.XPATH, "// input[ @ placeholder = 'Input your first name']")
        first_name.send_keys("Мой ответ")
        last_name = browser.find_element(By.XPATH, "// input[ @ placeholder = 'Input your last name']")
        last_name.send_keys("Мой ответ")
        email = browser.find_element(By.XPATH, "// input[ @ placeholder = 'Input your email']")
        email.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual_welcome_text = welcome_text_elt.text
        # ожидаемый текст приветствия
        expected_welcome_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # self.assertEqual('что должно быть', 'что есть', 'что произошло')
        assert expected_welcome_text == actual_welcome_text, 'You doing something wrong'  # add assertion here

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    pytest.main()
