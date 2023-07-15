from selenium.webdriver.common.by import By
from Base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

class Item_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ЛОКАТОРЫ"""

    add_cart = '/html/body/div[1]/div/section/div/section/section/div[3]/div[4]/a[1]'
    name_card = 'body > div.main > div > section > div > section > section > div.top_info.flex.right > h1'
    price_card = 'body > div.main > div > section > div > section > section > div.dataCol_r.right > div.box_price.flex > div > div.radio_price > label > div > div'
    book_in_store = '//a[@class="book_now modal_link"]'
    keep_shopping = '//*[@id="inCart_modal"]/div[4]/a[2]'
    shop = '#contentMap > ul > li:nth-child(1) > a.from-list.book_now.quick-order.modal_link'
    name = '#modal_quickstore_1 > form > div:nth-child(2) > input'
    mail = '#modal_quickstore_1 > form > div:nth-child(3) > input'
    phone = '#modal_quickstore_1 > form > div:nth-child(4) > input'
    close = '#fancybox-container-2 > div.fancybox-inner > div.fancybox-stage > div > div > button > svg'
    book = '#modal_quickstore_1 > form > div.box_btn.flex > div > button'

    """ПОЛУЧЕНИЕ ДАННЫХ"""
    def get_add_cart(self):#Кнопка добавления в корзину
        return self.driver.find_element(By.XPATH, self.add_cart)
    def get_price_card(self):#Сохранение цены в карточке товара
        return self.driver.find_element(By.CSS_SELECTOR, self.price_card)
    def get_name_card(self):#Сохранение имени в карточке товара
        return self.driver.find_element(By.CSS_SELECTOR, self.name_card)
    def get_book_in_store(self):#Кнопка брони в магазине
        return self.driver.find_element(By.XPATH, self.book_in_store)
    def get_keep_shopping(self):#Кнопка продолжить покупки
        return self.driver.find_element(By.XPATH, self.keep_shopping)
    def get_shop(self):#Получения локатора магазина для самовывоза
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.shop)))
    def get_name(self):#Локатор поля имени брони
        return self.driver.find_element(By.CSS_SELECTOR, self.name)
    def get_mail(self):#Локатор поля почты брони
        return self.driver.find_element(By.CSS_SELECTOR, self.mail)
    def get_phone(self):#Локатор телефона брони
        return self.driver.find_element(By.CSS_SELECTOR, self.phone)
    def get_book(self):#Локатор кнопки брони
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.book)))
    def get_close(self):#Кнопка закрытия окна
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.close)))
    def get_catalog(self, platform):#Локатор раздела
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/'+platform+'"]')))
    def get_card_price(self):#Цена карточки
        return self.driver.find_element(By.CSS_SELECTOR, self.price_card)
    def get_card_name(self):#Имя карточки
        return self.driver.find_element(By.CSS_SELECTOR, self.name_card)

    """МЕТОДЫ В КАРТОЧКЕ ТОВАРА"""
    def add_to_cart(self):#Клик на добавление в корзину
        self.get_add_cart().click()
        print('Добавили в корзину из карточки')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Добавили в корзину ' \
                                    + self.date + '.png')
    def book_item(self):#Клик на бронь
        self.get_book_in_store().click()
        print('Забронировали товар')
    def keep_going(self):#Клик на продолжить покупки
        self.get_keep_shopping().click()
        print('Кликнули "Продолжить покупки"')
    def choose_shop(self):#Выбор магазина для самовывоза
        self.get_shop().click()
        print('Выбрали магазин для брони')
    def put_name(self):#Установка имени
        self.get_name().send_keys('Иван')
        print('Ввели имя')
    def put_mail(self):#Установка почты для брони
        self.get_mail().send_keys('123@123.ru')
        print('Ввели почту')
    def put_phone(self):#Установка телефона для брони
        self.get_phone().send_keys('9999999999')
        print('Ввели телефон')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Окно оповещения + ' \
                                    + self.date + '.png')
    def close_modul(self):#Закрытие окна
        self.get_close().click()
        print('Закрыли')
    def go_on(self, addit):#Переход к каталогу
        self.get_catalog(addit).click()
        print('Перешли в раздел каталога')

    def orig_price_read(self):#Проверка корректности цены
        fs = open('orig_price.txt', 'r', encoding='utf-8')
        value = fs.read()
        value1 = self.get_card_price().text
        try:
            assert value == value1
            print('Цена верная')
        except AssertionError:
            print('АЛЯРМ!!! Цена неверная')

    def orig_name_read(self):#Проверка корректности имени
        fs = open('orig_name.txt', 'r', encoding='utf-8')
        value = fs.read()
        value1 = self.get_card_name().text
        try:
            assert value == value1
            print('Название верное')
        except AssertionError:
            print('АЛЯРМ!!! Название неверное')

    """СЦЕНАРИИ РАБОТЫ С КАРТОЧКОЙ ТОВАРА"""
    def add_and_go(self, where):#Добавить в корзину и продолжить покупки
        self.orig_name_read()
        self.orig_price_read()
        self.add_to_cart()
        self.keep_going()
        self.go_on(where)#Метод требует указания платформы из списка urls в файле теста
        print('')

    def book_and_go(self):#Забронировать товар и отправиться дальше
        self.orig_name_read()
        self.book_item()
        self.choose_shop()
        self.put_name()
        self.put_mail()
        self.put_phone()
        self.close_modul()
        print('')