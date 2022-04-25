from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_css_selector('input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.XPATH, "// button[ @ type = 'submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

