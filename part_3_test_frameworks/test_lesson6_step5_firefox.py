from selenium import webdriver
from conftest import browser_firefox


# Инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
class TestParam:
    link = "https://stepik.org/lesson/25969/step/8"

    def test_use_links(self, browser_firefox):
        browser_firefox.get(self.link)
