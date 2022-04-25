import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # inversion:   'pytest -s -v -m "not smoke" test_lesson5_step3_mark_types.py'
    # combination: 'pytest -s -v -m "smoke
    #              or regression" test_lesson5_step3_mark_types.py' тоесть запускается если маркировка smoke или
    #              regression
    #              'pytest -s -v -m "smoke and win10" test_lesson5_step3_mark_types.py ' тоесть запускается если
    #              маркировка smoke и win10 (обязательно должны быть обе)
