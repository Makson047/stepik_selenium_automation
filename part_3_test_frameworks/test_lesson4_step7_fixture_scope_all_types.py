import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("^_^", "\n")
    browser = webdriver.Chrome()
    yield browser
    print(":3", "\n")
    browser.quit()


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces:
    def test_first_smiling_faces(self, browser, very_important_fixture):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_second_smiling_faces(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
