from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.gamepark.ru/'
    search = '#title-prop-search-input'
    loccheck = 'body > div.main > div > section.popular_cats > div > div.main_title'
    def get_catalog(self, platform):#Получение локатора раздела на сайте
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/'+platform+'"]')))
    def get_search(self):#Получение локатора меню поиска
        return WDW(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search)))

    def search_thing(self, object):#Начало поиска
        self.get_search().send_keys(object)
        print('Ввели поисковый запрос')
        self.get_search().send_keys(Keys.ENTER)
        print('Нажали энтер')
    def buy_thing(self, choose_param):#Переход на раздел каталога
        self.get_catalog(choose_param).click()#В файле теста необходимо указать желаемый параметр из списка urls
        print('Перешли на страницу раздела')
        self.driver.save_screenshot('C:\\Users\\Igor\\PycharmProjects\\final_stuff\\screen\\ Перешли на страницу раздела + ' \
                                    + self.date + '.png')
        print('')