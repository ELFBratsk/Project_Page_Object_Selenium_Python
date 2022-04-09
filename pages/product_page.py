from unicodedata import name
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click() # метод для добавления в корзину
        
    def should_to_basket(self): # методы-проверки
        assert self.is_element_present(*ProductPageLocators.MESSAGES_ITEMS), "MESSAGES_ITEMS is not presented"
        assert self.browser.find_element(*ProductPageLocators.CONTENT_INNER).text == self.browser.find_element(*ProductPageLocators.BASKET_ITEMS).text, "Название книги не совпадает"
        assert self.browser.find_element(*ProductPageLocators.PRICE_ITEMS).text == self.browser.find_element(*ProductPageLocators.PRICE_TO_BASKET).text, "Цены не совпадают"   
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_ITEMS), \
       "Success message is presented, but should not be"
    
    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES_ITEMS), \
       "Success message is presented, but should not be"