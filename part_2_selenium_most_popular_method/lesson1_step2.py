from selenium import webdriver
browser = webdriver.Chrome()

# for checkbox and radiobutton
option1 = browser.find_element_by_css_selector("[value='python']")
option1.click()

# ot click on label element
option1 = browser.find_element_by_css_selector("[for='java']")
option1.click()
