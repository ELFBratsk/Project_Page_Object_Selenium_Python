from selenium.common.exceptions import NoSuchElementException # Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class BasePage():
    def __init__(self, browser, url, timeout=10): # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:
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