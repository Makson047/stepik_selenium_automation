"""
   Структура:
1. Фикстура browser. как в предыдущих примерах.
2. Класс, который начинается на Test. Как в предыдущих примерах.
3. Внутри класса 2 переменные:
    - пустая для сообщения = "".
    - массив со списком адресов
4. Внутри класса также есть функция с parametrize('название переменной для использования внутри этой функции= неважно
   какое, но желательно подходящее по смыслу я назову links', "название переменой массива со списком адресов") похожее
   на предыдущий урок.
5. Эта функция тест поэтому название функции должно начинаться на test_
6. Эта функция получает self, browser, и название переменной для использования внутри этой функции (с 4 пункта ''
   я назову links например).

Внутри функции:
7.  Первые 2 строчки как в предыдущем примере 2 предпоследние с небольшим изменением в link.
8.  browser.implicity_wait(10)
9.  Ищем textarea.
10. Записываем в неё через  send_key(str(math.log(int(time.time())))  с примера.
11. Через WebDriverWait EC.element_to_be_clickable находим класс кнопку.
12. нажимаем на кнопку
13. Через WebDriverWait EC.visibility_of_element_located().text находим класс сообщения и текст его присваиваем
    переменной.
14. Проверяем не равен ли он !="Correct!"
15. если не равен то добавляем в переменную с 4 пункта посредством self. название переменной += с пункта 13 пунк
    переменная и print().
16. assert с пункта13  переменная == False проверяем
17.
    if __name__ == "__main__":
        unittest.main()
"""

import math
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestParam:
    msg = ''
    links_list = ['https://stepik.org/lesson/236895/step/1',
                  'https://stepik.org/lesson/236896/step/1',
                  'https://stepik.org/lesson/236897/step/1',
                  'https://stepik.org/lesson/236898/step/1',
                  'https://stepik.org/lesson/236899/step/1',
                  'https://stepik.org/lesson/236903/step/1',
                  'https://stepik.org/lesson/236904/step/1',
                  'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('links', links_list)
    def test_use_links(self, browser, links):
        browser.get(links)
        browser.implicitly_wait(10)

        browser.find_element_by_css_selector(".textarea").send_keys(str(math.log(int(time.time() - 0.7))))

        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()

        actual_feedback_elm = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        actual_feedback = actual_feedback_elm.text
        expected_feedback = 'Correct!'

        if actual_feedback != 'Correct!':
            self.msg += actual_feedback
            print(self.msg)

        assert expected_feedback == actual_feedback, "Your answer is wrong!"
