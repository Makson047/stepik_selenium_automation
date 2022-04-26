import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
        Опция командной строки.
        В командную строку передается параметр вида '--browser_name="firefox"'
        По умолчанию передается параметр, запускающий Chrome браузер
    """
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")
    """
        Опция командной строки.
        В командную строку передается параметр вида '--language="es"'
        По умолчанию передается параметр, включающий английский интерфейс в браузере
    """
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: ua, ru, en, es ... (etc.)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption('language')

    if browser_name == "chrome":
        print("\nStart chrome browser for test..")

        # Инициализируются опции браузера
        options = Options()

        # В опции веб драйвера передаем параметр из командной строки
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', 'user_language')
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)
    yield browser
    print("\nQuit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def chrome():
    print("\nStart browser for test..")
    chrome = webdriver.Chrome()
    yield chrome
    print("\nQuit browser..")
    chrome.quit()


@pytest.fixture(scope="function")
def firefox():
    print("\nStart browser for test..")
    firefox = webdriver.Firefox()
    yield firefox
    print("\nQuit browser..")
    firefox.quit()
