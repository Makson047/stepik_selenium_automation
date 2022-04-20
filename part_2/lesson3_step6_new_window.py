from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()

    first_window = browser.window_handles[0]  # save present window name
    new_window = browser.window_handles[1]  # save new window name
    browser.switch_to.window(new_window)  # switch to new window

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_css_selector("[id='input_value']").text
    y = calc(x)

    answer = browser.find_element(By.XPATH, "// input[ @ id = 'answer']").send_keys(y)

    button = browser.find_element_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
