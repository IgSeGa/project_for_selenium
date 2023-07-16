from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
class Category_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ЛОКАТОРЫ"""

    price_min = '//input[@class="input ot"]'
    slider_min = 'body > div.main > div > section > div > section > aside > div > form > div:nth-child(3) > div.range.price_range > span > span.irs-slider.from'
    price_max = '//input[@class="input do"]'
    slider_max = 'body > div.main > div > section > div > section > aside > div > form > div:nth-child(3) > div.range.price_range > span > span.irs-slider.to'
    calendar = '//input[@name="DATE_RELEASE"]'
    publusher = '/html/body/div[1]/div/section/div/section/aside/div/form/div[4]/div[2]'
    publisher_click = '//div[@data-value="4597"]'
    genre = '/html/body/div[1]/div/section/div/section/aside/div/form/div[6]/div[2]/div/div[1]'
    genre_click = '//div[@data-value="128"]'
    age = '/html/body/div[1]/div/section/div/section/aside/div/form/div[7]/div[2]/div/div[1]'
    age_click = '//div[@data-value="342"]'
    sub_button = 'body > div.main > div > section > div > section > aside > div > form > div.item_btn > div.submit > button'
    item_plash = 'body > div.main > div > section > div > section > div > section.products > div > div'
    check_hit = 'body > div.main > div > section > div > section > aside > div > form > div:nth-child(2) > div:nth-child(2) > label'
    check_sale = 'body > div.main > div > section > div > section > aside > div > form > div:nth-child(2) > div:nth-child(3) > label'
    consoles = 'body > div.main > div > section > div > section > div > section.category > div > a:nth-child(2)'
    accessories = 'body > div.main > div > section > div > section > div > section.category > div > a:nth-child(1)'
    learn = 'body > div.main > div > section > div > section > div > section.products > div > div > div.box_btn.flex > a.subscribe_no_by.modal_link'
    input_notification = '//input[@name="contact[1][user]"]'
    close_learn = '//button[@class="fancybox-button fancybox-close-small"]'
    arrow_right = 'body > div.main > div > section > div > section > div > section.products > section > a.next'
    arrow_left = 'body > div.main > div > section > div > section > div > section.products > section > a.prev'
    law = 'body > div.main > div > section > div > section > div > section.products > div > div:nth-child(11) > div.block > div.name > a'
    page1 = 'body > div.main > div > section > div > section > div > section.products > section > a:nth-child(2)'
    ulti = 'body > div.main > div > section > div > section > div > section.products > div > div:nth-child(17) > div.block > div.name > a'
    go_cart = '//*[@id="inCart_modal"]/div[4]/a[1]'
    orig_price = '/html/body/div[1]/div/section/div/section/div/section[3]/div/div/div[4]/div/div[2]/label/div/div'
    orig_name = 'body > div.main > div > section > div > section > div > section.products > div > div > div.block > div.name > a'
    orig_name1 = 'body > div.main > div > section > div > section > div > section.products > div > div:nth-child(17) > div.block > div.name > a'
    absent = 'body > div.main > div > section > div > section > div > p'

    """ПОЛУЧЕНИЕ ЭЛЕМЕНТОВ"""
    def get_price_min(self):#Получение поля минимальной цены
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))
    def get_price_max(self):#Получение поля максимальной цены
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))
    def get_slider_min(self):#Получение левого ползунка слайдера цены
        return self.driver.find_element(By.CSS_SELECTOR, self.slider_min)
    def get_slider_max(self):#Получение правого ползунка слайдера цены
        return self.driver.find_element(By.CSS_SELECTOR, self.slider_max)
    def get_calendar(self):#Получение календаря
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calendar)))
    def get_publisher(self):#Получение селектора издателей
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.publusher)))
    def get_publisher_click(self):#Получение конкретного издателя
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.publisher_click)))
    def get_genre(self):#Получение селектора жанра
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.genre)))
    def get_genre_click(self):#Получение конкретного жанра
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.genre_click)))
    def get_age(self):#Получение селектора возрастного ограничения
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age)))
    def get_age_click(self):#Получение конкретного возраста
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_click)))
    def get_sub_button(self):#Получение поля минимальной цены
        return self.driver.find_element(By.CSS_SELECTOR, self.sub_button)
    def get_item(self):#Получение карточки товара
        return self.driver.find_element(By.CSS_SELECTOR, self.item_plash)
    def get_hit(self):#Получение чекбокса хит
        return self.driver.find_element(By.CSS_SELECTOR, self.check_hit)
    def get_sale(self):#Получение чекбокса распродажа
        return self.driver.find_element(By.CSS_SELECTOR, self.check_sale)
    def get_accessories(self):#Кнопка раздела аксессуары
        return self.driver.find_element(By.CSS_SELECTOR, self.accessories)
    def get_consoles(self):#Кнопка раздела консоли
        return self.driver.find_element(By.CSS_SELECTOR, self.consoles)
    def get_learn(self):#Кнопка "Узнать о поступлении"
        return self.driver.find_element(By.CSS_SELECTOR, self.learn)
    def get_put_notification(self):#Кнопка внесения данных о нотификации
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_notification)))
    def get_close_learn(self):#Кнопка закрытия всплывающего окна
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_learn)))
    def get_arrow_left(self):#Стрелка влево
        return self.driver.find_element(By.CSS_SELECTOR, self.arrow_left)
    def get_arrow_right(self):#Стрелка вправо
        return self.driver.find_element(By.CSS_SELECTOR, self.arrow_right)
    def get_law(self):#Товар на третьей странице
        return self.driver.find_element(By.CSS_SELECTOR, self.law)
    def get_page1(self):#Переход к первой странице
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.page1)))
    def get_ulti(self):#Товар на первой странице
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.ulti)))
    def get_orig_price(self):#Получение изначальной цены товара
        return self.driver.find_element(By.XPATH, self.orig_price)
    def get_orig_name(self):#Получение изначального имени товара
        return self.driver.find_element(By.CSS_SELECTOR, self.orig_name)
    def get_orig_name1(self):#Получение имени второго товара
        return self.driver.find_element(By.CSS_SELECTOR, self.orig_name1)
    def get_absent(self):#Метод получения сообщения об отсутствии товаров
        return self.driver.find_element(By.CSS_SELECTOR, self.absent)


    """МЕТОДЫ РАБОТЫ С ЭЛЕМЕНТАМИ"""
    def set_price_min(self, min):#Установка минимальной цены
        self.get_price_min().clear()
        self.get_price_min().send_keys(min)
        print('Ввели минимальную цену')
    def set_price_max(self, max):#Установка максимальной цены
        self.get_price_max().clear()
        self.get_price_max().send_keys(max)
        print('Ввели максимальную цену')
    def slide_price_min(self, x, y):#Установка минимальной цены слайдером
        actions = ActionChains(self.driver)
        actions.click_and_hold(self.get_slider_min()).move_by_offset(x, y).release().perform()
        print('Подвинули левый слайдер')
    def slide_price_max(self, x, y):#Установка максимальной цены слайдером
        actions = ActionChains(self.driver)
        actions.click_and_hold(self.get_slider_max()).move_by_offset(x, y).release().perform()
        print('Подвинули правый слайдер')
    def set_date(self, delta):#Установка даты
        import datetime
        date = datetime.datetime.utcnow().strftime('%d.%m.%Y')
        update = datetime.timedelta(delta)
        from datetime import datetime
        newdate = datetime.strptime(date, '%d.%m.%Y').date()
        plusdate = newdate + update
        ultradate = datetime.strftime(plusdate, '%d.%m.%Y')
        self.get_calendar().click()
        self.get_calendar().send_keys(ultradate)
        print('Сместили дату')
    def set_publisher(self):#Установка издателя
        self.get_publisher().click()
        try:
            self.get_publisher_click().click()
            print('Выбрали издателя')
        except TimeoutException:
            print('ИЗМЕНИ ИЗДАТЕЛЯ, ПОДХОДЯЩЕГО НЕТ')
            self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Нет издателя ' \
                                        + self.date + '.png')
            quit()
    def set_genre(self):#Установка жанра
        try:
            self.get_genre().click()
            self.get_genre_click().click()
            print('Выбрали жанр')
        except TimeoutException:
            print('ИЗМЕНИ ЖАНР, ПОДХОДЯЩЕГО НЕТ')
            self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Нет жанра ' \
                                        + self.date + '.png')
            quit()
    def set_age(self):#Установка возрастного ограничения
        try:
            self.get_age().click()
            self.get_age_click().click()
            print('Выбрали возрастное ограничение')
        except TimeoutException:
            print('ИЗМЕНИ ВОЗРАСТ, ПОДХОДЯЩЕГО НЕТ')
            self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Нет возраста ' \
                                        + self.date + '.png')
            quit()
    def do_submit(self):#Применение изменений
        self.get_sub_button().click()
        print('Применили изменения')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Применили изменения ' \
                                    + self.date + '.png')
    def go_to_card(self):  # Переход в карточку товара
        try:
            self.get_item().click()
            print('Перешли в карточку товара')
        except NoSuchElementException:
            try:
                a = self.get_absent().text
                assert a == 'В данной категории нет товаров, или фильтр задан слишком строго.'
                print('ИЗМЕНИ ПАРАМЕТРЫ, нет подходящих товаров')
            except NoSuchElementException:
                print('АЛЯРМ!!! СО СТРАНИЦЕЙ ЧТО-ТО НЕ ТАК!!!')

    def switch_to_consoles(self):#Переключение на раздел консолей
        self.get_consoles().click()
        print('Перешли в раздел "Консоли"')
    def switch_to_accessories(self):#Переключение на раздел аксессуаров
        self.get_accessories().click()
        print('Перешли в раздел "Аксессуары"')
    def click_hit(self):#Клик на чекбокс хит
        self.get_hit().click()
        print('Выбрали чекбокс "Хит"')
    def click_sale(self):#Клик на чекбокс распродажа
        self.get_sale().click()
        print('Выбрали чекбокс "Распродажа"')
    def do_learn(self):#Метод подписки на поступление товара. Здесь заканчивается ничем, чтобы не спамить магазину
        try:
            self.get_learn().click()
            self.get_put_notification().send_keys('123@123.ru')
            print('Ввели данные сообщения о поступлении')
            self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Окно оповещения ' \
                                    + self.date + '.png')
        except NoSuchElementException:
            try:
                a = self.get_absent().text
                assert a == 'В данной категории нет товаров, или фильтр задан слишком строго.'
                print('ИЗМЕНИ ПАРАМЕТРЫ ТЕСТА, ПОД ИМЕЮЩИЕСЯ НЕТ ТОВАРА')
                self.driver.save_screenshot(
                    'C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Нет товара ' \
                    + self.date + '.png')
                quit()
            except AssertionError:
                print('Что-то сломалось на странице')
                self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Поломка кнопки оповещения ' \
                                            + self.date + '.png')
                quit()
    def do_close_learn(self):#Закрытие окна нотификации
        self.get_close_learn().click()
        print('Нотификация закрыта')
    def click_left(self):#Клик на левую стрелку
        self.get_arrow_left().click()
    def click_right(self):#Клик на правую стрелку
        try:
            self.get_arrow_right().click()
            print('Кликнули стрелку вправо')
        except NoSuchElementException:
            try:
                a = self.get_absent().text
                assert a == 'В данной категории нет товаров, или фильтр задан слишком строго.'
                print('ИЗМЕНИ ПАРАМЕТРЫ ТЕСТА, ПОД ИМЕЮЩИЕСЯ НЕТ ТОВАРА')
                self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Нет товара ' \
                        + self.date + '.png')
                quit()
            except AssertionError:
                print('АЛЯРМ! Стрелка не прожимается')
                self.driver.execute_script('window.scrollTo(0, 1000)')
                self.driver.save_screenshot('Стрелка почему-то не нажалась.png')
    def d_water_law(self):#Переход в карточку товара на 3 странице
        self.get_law().click()
        print('Зашли в товар')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Зашли в товар на 3 странице + ' \
                                    + self.date + '.png')
    def go_page1(self):#Переход на 1 страницу
        self.get_page1().click()
        print('Кликнули на первую страницу')
    def buy_ulti(self):#Переход в товар на первой странице
        self.get_ulti().click()
        print('Перешли в товар с первой страницы')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Зашли в товар на 1 странице + ' \
                                    + self.date + '.png')
    def print_orig_price(self):#Запоминание цены на общей странице товаров
        try:
            value_price = self.get_orig_price().text
            fs = open('orig_price.txt', 'w', encoding='utf-8')
            fs.write(value_price)
        except NoSuchElementException:
            try:
                a = self.get_absent().text
                assert a == 'В данной категории нет товаров, или фильтр задан слишком строго.'
                print('ИЗМЕНИ ПАРАМЕТРЫ ТЕСТА, ПОД ИМЕЮЩИЕСЯ НЕТ ТОВАРА')
                self.driver.save_screenshot(
                    'C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Нет товара ' \
                    + self.date + '.png')
                quit()
            except AssertionError:
                print('Что-то сломалось на странице')
                self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Поломка кнопки оповещения ' \
                                            + self.date + '.png')
                quit()
    def print_orig_name(self):#Запоминание имени на общей странице товаров
        value_name = self.get_orig_name().text
        fs = open('orig_name.txt', 'w', encoding='utf-8')
        fs.write(value_name)
    def url_orig(self):#Запоминание урла для дальнейшего референса
        x = self.driver.current_url
        fs = open('orig_url.txt', 'w')
        fs.write(x)
    def compare_url(self):#Определение корректности урл страницы
        fs = open('orig_url.txt', 'r')
        a = fs.read()
        b = self.driver.current_url
        try:
            assert b == a
            print('Страница правильная')
        except AssertionError:
            try:
                assert b == a[:55]
                print('Перешли на первую страницу')
            except AssertionError:
                print('АЛЯРМ!! СТРАНИЦА НЕВЕРНАЯ!!!')
    def write_orig_name1(self):#Запись второго названия, затирает первое, сделано для разных тестов
        value_name = self.get_orig_name1().text
        fs = open('orig_name.txt', 'w', encoding='utf-8')
        fs.write(value_name)

    """ТЕСТОВЫЕ СЦЕНАРИИ НА СТРАНИЦАХ КАТЕГОРИЙ"""
    def set_params_to_buy(self):#Выбор товара через ручную установку параметров и страницы игр
        self.set_price_min('1000')#Требуется вручную установить минимальную цену
        self.set_price_max('6000')#Требуется вручную установить максимальную цену
        self.set_date(-150)#Требуется вручную установить промежуток времени от текущей даты до даты начала продаж
        self.set_publisher()
        self.set_genre()
        self.set_age()
        self.do_submit()
        self.print_orig_price()
        self.print_orig_name()
        self.go_to_card()
        print('')

    def set_params_to_notify(self):#Оставление заявки на оповещение о поступлении кончившегося товара и страницы консолей
        self.switch_to_consoles()
        self.click_hit()
        self.click_sale()
        self.slide_price_min(10, 0)#Требуется вручную установить необходимый сдвиг левого ползунка
        self.slide_price_max(-80, 0)#Требуется вручную установить необходимый сдвиг правого ползунка
        self.do_submit()
        self.do_learn()
        self.do_close_learn()#Используется метод закрытия, чтобы не создавать спам для магазина
        print('')

    def set_param_accessory(self):#Проверка работы страницы посика и раздела аксессуаров
        self.switch_to_accessories()
        self.click_right()
        self.click_right()
        self.url_orig()
        self.d_water_law()
        self.go_back()
        self.compare_url()
        self.go_page1()
        self.compare_url()
        self.write_orig_name1()
        self.buy_ulti()
        print('')