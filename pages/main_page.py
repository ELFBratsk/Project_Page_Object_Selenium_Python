from .base_page import BasePage
#from .locators import MainPageLocators

# В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку: 
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

# ИЛИ ТАК:
'''class MainPage(BasePage):
    pass '''
        
'''class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
              
   
    def should_be_login_link(self): 
        # Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке:       
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" '''