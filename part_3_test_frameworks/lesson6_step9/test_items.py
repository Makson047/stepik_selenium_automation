import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_basket_exists(browser):
    """
    Тест проверяет, что страница товара
    содержит кнопку добавления в корзину
    """

    # Открываем страницу товара
    browser.get(link)

    # Установлено время принудительной задержки браузера
    # после открытия страницы, для визуальной проверки языка открытой страницы
    time.sleep(10)

    # Проверяем наличие кнопки добавления товара в корзину
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, 'Your element does not exist'
