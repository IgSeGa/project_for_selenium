import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.category_page import Category_page
from pages.item_card import Item_page
from pages.cart import Cart
from Base.base_class import Base


driver = webdriver.Chrome()
urls = ['playstation5/games/', 'playstation4/games/', 'xboxone/games/', 'switch/games/', 'pc/games/',\
        'boardgames/games/', 'souvenirs/?PROPERTY_PUBLISHER=82761', 'souvenirs/', 'comics/', 'used/games/', \
        'preorder/games/?sort=date_release', 'news/?type=action']  # Список локаторов для индексных страниц товаров

"""ПОКУПКА ТОВАРА И ПРОВЕРКА СТРАНИЦЫ ИГР"""
@pytest.mark.run(order=3)
def test_buy(set_up):
    base = Base(driver)
    base.begin_test()
    main = Main_page(driver)
    main.buy_thing(urls[3])  # Необходимо добавить параметр локатора из списка urls. Диапазон 0-11
    cat = Category_page(driver)
    cat.set_params_to_buy()
    item = Item_page(driver)
    item.add_and_go(urls[6])  # Необходимо добавить параметр локатора из списка urls. Диапазон 0-11
    cart = Cart(driver)
    cart.finish()
"""ЗАЯВКА НА УВЕДОМЛЕНИЕ О ПОСТУПЛЕНИИ ТОВАРА И ПРОВЕРКА СТРАНИЦЫ КОНСОЛЕЙ"""
@pytest.mark.run(order=1)
def test_notify(set_up):
    base = Base(driver)
    base.begin_test()
    main = Main_page(driver)
    main.buy_thing(urls[2])  # Необходимо добавить параметр локатора из списка urls. Диапазон 0-11
    cat = Category_page(driver)
    cat.set_params_to_notify()

"""ПРОВЕРКА РАБОТЫ СТРАНИЦЫ ПОИСКА В РАЗДЕЛЕ СУВЕНИРОВ"""
@pytest.mark.run(order=2)
def test_search_page(set_up):
    base = Base(driver)
    base.begin_test()
    main = Main_page(driver)
    main.search_thing('one piece')  # Необходимо ввести запрос для поиска
    cat = Category_page(driver)
    cat.set_param_accessory()
    item = Item_page(driver)
    item.book_and_go()