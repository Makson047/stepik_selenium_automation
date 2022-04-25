"""Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на результаты выполнения следующего теста,
поэтому лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее. К тому же если вдруг
браузер зависнет в одном тесте, то другие тесты не пострадают, если они запускаются каждый в собственном браузере. """

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1:
    # создание экземпляра браузера и его закрытие только один раз для всех тестов
    @classmethod
    def setup_class(cls):
        print("\nstart browser for test suite..")
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("quit browser for test suite..")
        cls.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2:  # The best decision!!!
    # создание браузера для каждого теста
    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
