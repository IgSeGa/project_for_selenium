from selenium.webdriver.common.by import By
from Base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

class Cart(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ЛОКАТОРЫ"""

    cart = 'body > div.main > div > header > div.info > div > a.cart'
    cart_name = '#basket_form > div > div.cart_info > div > div > div.top.flex > div.box_info > div.name > a'
    cart_price = '#basket_form > div > div.cart_info > div > div > div.top.flex > div.box_price > div.price'
    final_price = '#stick_box > div:nth-child(5) > div > div.price'
    to_checkout = '#stick_box > a'
    fio = '#ORDER_PROP_2'
    mail = '#ORDER_PROP_3'
    phone = '#ORDER_PROP_4'
    comment = '#message'
    checkout_name = '#ORDER_FORM_ID_NEW > section:nth-child(8) > div > section > div:nth-child(2) > div.order_list.flex > div > div > div.name > a'
    checkout_price = '#ORDER_FORM_ID_NEW > section:nth-child(8) > div > section > div:nth-child(2) > div.order_list.flex > div > div > div.bot.flex > div.price'
    selector = '#pickup > div.line_form > div > div'
    shop = '#pickup > div.line_form > div > div > div.list > div > div:nth-child(5)'
    cash = '#ORDER_FORM_ID_NEW > section:nth-child(8) > div > section > div:nth-child(4) > div.box_radio > div:nth-child(1) > label > div'
    order = '#ORDER_FORM_ID_NEW > section:nth-child(9) > div > section > div > div.submit > button'

    """МЕТОДЫ ПОЛУЧЕНИЯ ТОВАРОВ"""
    def get_cart(self):#Получение корзины
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart)))
    def get_cart_name(self):#Получение имени товара в корзине
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart_name)))
    def get_cart_price(self):#Получение цены товара в корзине
            return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart_price)))
    def get_final_price(self):#Получение итоговой цены товара
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.final_price)))
    def get_to_checkout(self):#Кнопка перехода к оформлению
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.to_checkout)))
    def get_fio(self):#Получение ФИО
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.fio)))
    def get_mail(self):#Получение почты
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.mail)))
    def get_phone(self):#Получение телефона
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.phone)))
    def get_comment(self):#Получение коммента
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.comment)))
    def get_checkout_name(self):#Получение имени на чекауте
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkout_name)))
    def get_checkout_price(self):#Получение цены
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkout_price)))
    def get_selector(self):#Получение селектора магазинов
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selector)))
    def get_shop(self):#Получение конкретного магазина
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.shop)))
    def get_cash(self):#Получение выбора наличных
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cash)))
    def get_order(self):#Получение конопки заказа
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.order)))

    """МЕТОДЫ РАБОТЫ С КОРЗИНОЙ"""
    def go_to_cart(self):
        self.get_cart().click()
        print('В корзину перешли')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ В корзине + ' \
                                    + self.date + '.png')
    def go_checkout(self):
        self.get_to_checkout().click()
        print('Перешли на чекаут')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Перешли к оплате + ' \
                                    + self.date + '.png')
    def put_fio(self):
        self.get_fio().send_keys('Иван Иванов')
        print('Ввели имя')
    def put_mail(self):
        self.get_mail().send_keys('123@123.ru')
        print('Ввели почту')
    def put_phone(self):
        self.get_phone().send_keys('9999999999')
        print('Ввели телефон')
    def leave_comment(self):
        self.get_comment().send_keys('Вас заавотестили')
        print('Оставили комментарий')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Данные в корзине + ' \
                                + self.date + '.png')
    def choose_shop(self):
        self.get_selector().click()
        self.get_shop().click()
        print('Открыли селектор')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Открыт селектор + ' \
                                + self.date + '.png')
    def choose_cash(self):
        self.get_cash().click()
        print('Выбрали нал')
    def orig_price_read(self):
        fs = open('orig_price.txt', 'r', encoding='utf-8')
        value = fs.read()
        value1 = self.get_cart_price().text
        try:
            assert value == value1
            print('Цена в корзине верная')
        except AssertionError:
            print('АЛЯРМ!!! Цена в корзине неверная')

    def orig_name_read(self):
        fs = open('orig_name.txt', 'r', encoding='utf-8')
        value = fs.read()
        value1 = self.get_cart_name().text
        try:
            assert value == value1
            print('Название корзины верное')
        except AssertionError:
            print('АЛЯРМ!!! Название неверное')
    def chekout_price_read(self):
        fs = open('orig_price.txt', 'r', encoding='utf-8')
        value = fs.read()
        value1 = self.get_checkout_price().text
        try:
            assert value == value1
            print('Цена чекаута верная')
        except AssertionError:
            print('АЛЯРМ!!! Цена неверная')

    def checkout_name_read(self):
        fs = open('orig_name.txt', 'r', encoding='utf-8')
        value = fs.read()
        value1 = self.get_checkout_name().text
        try:
            assert value == value1
            print('Название чекаута верное')
        except AssertionError:
            print('АЛЯРМ!!! Название неверное')
    def do_order(self):
        self.get_order().click()

    """ОФОРМЛЕНИЕ ЗАКАЗА"""
    def finish(self):
        self.go_to_cart()
        self.orig_name_read()
        self.orig_price_read()
        self.go_checkout()
        self.checkout_name_read()
        self.chekout_price_read()
        self.put_fio()
        self.put_mail()
        self.put_phone()
        self.leave_comment()
        self.choose_shop()
        self.choose_cash()#Тест заканчивается на этом, так как не хочу создавать спам магазину. Метод для кнопки сам по себе есть
        print('')