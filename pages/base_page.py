from selenium.common.exceptions import NoSuchElementException # Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=7): # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url) #Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get()
    
    # Теперь в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).     
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException): # except (имя исключения):
            return False
        return True
    
    # Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(), который приведен ниже. Например, можете добавить его в класс BasePage
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    # Можно добавить в BasePage абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    # Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем: 
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    
    # В файл base_page.py переносим соответствующие методы, заменяя класс с локаторами на BasePageLocators:  
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented" 
    
    # В классе BasePage реализуйте соответствующий метод для перехода в корзину  
    def should_be_basket_page(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BTN), "Login link is not presented" # проверяем что кнопка есть
        
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BTN) # переходим в корзину
        link.click()
    
    # Добавьте в BasePage проверку того, что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
    