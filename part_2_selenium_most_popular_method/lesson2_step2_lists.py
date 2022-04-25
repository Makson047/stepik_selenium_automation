from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(2)").click()
    # or
    # browser.find_element_by_css_selector("[value='58']").click()

    # or
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value("79")  # ищем элемент по value
    # or
    # select.select_by_visible_text("text")  # по видимому тексту
    # or
    # select.select_by_index(1)  # По индексу или порядковому номеру. Индексация начинается с нуля

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
