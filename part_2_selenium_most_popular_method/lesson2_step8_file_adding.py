import os
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for element in elements:
        element.send_keys("Мой ответ")
    # // input[ @ placeholder = "Input your first name"]

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(current_dir, 'test.txt')

    select_file = browser.find_element_by_css_selector("input[type = 'file']")
    select_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
