from selenium import webdriver
import time


link1 = "https://rozetka.com.ua/asus-90nr03u2-m06330/p335388493/"
link2 = "https://rozetka.com.ua/hp-4a7m9ea/p332149516/"

try:
    browser = webdriver.Chrome()
    browser.get(link1)

    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector('.product-trade [aria-label="Купить"]')
    add_button.click()
    # time.sleep(30)

    # открываем страницу второго товара
    browser.get(link2)

    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector('.product-trade [aria-label="Купить"]')
    add_button.click()

    # find busket
    add_button = browser.find_element_by_css_selector('.header-actions .header__button--active')
    add_button.click()
    # ищем все добавленные товары
    goods = browser.find_elements_by_css_selector(".cart-list .cart-product__title")

    # проверяем, что количество товаров равно 2
    assert len(goods) == 2

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
