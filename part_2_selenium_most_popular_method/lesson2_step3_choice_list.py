from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calculate(number1, number2):
        return str(int(number1) + int(number2))

    num1 = browser.find_element_by_css_selector("#num1").text
    num2 = browser.find_element_by_css_selector("#num2").text
    y = calculate(num1, num2)

    select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(y)  # ищем элемент по value
    # or
    select.select_by_visible_text(y)  # по видимому тексту

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
