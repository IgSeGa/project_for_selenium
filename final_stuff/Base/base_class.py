import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver
    url = 'https://www.gamepark.ru/'
    date = datetime.datetime.utcnow().strftime('%d-%m-%Y, %H-%M-%S')

    def begin_test(self):#Инициация теста
        self.driver.get(self.url)
        a = self.driver.current_url
        assert a == self.url
        print('Открыта главная')
        self.driver.maximize_window()
        print('Окно открыто на полную')

    def go_back(self):#Возвращение на страницу назад
        self.driver.back()
        print('вернулись назад')