from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click() # метод для добавления в корзину
        
   
    def should_be_login_link(self): 
        # Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке:       
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Login link is not presented"