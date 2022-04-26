import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestParam:
    msg = ''
    link = 'https://stepik.org/lesson/236895/step/1'

    def test_use_links(self, chrome):
        chrome.get(self.link)
        chrome.implicitly_wait(10)

        chrome.find_element_by_css_selector(".textarea").send_keys(str(math.log(int(time.time() - 0.7))))
        button = WebDriverWait(chrome, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()

        actual_feedback_elm = WebDriverWait(chrome, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        actual_feedback = actual_feedback_elm.text
        expected_feedback = 'Correct!'

        if actual_feedback != 'Correct!':
            self.msg += actual_feedback
            print(self.msg)

        assert expected_feedback == actual_feedback, "Your answer is wrong!"
