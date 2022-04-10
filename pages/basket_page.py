from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_success_message_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGES_ITEMS), \
       "Success message is presented, but should not be" # Ожидаем, что в корзине нет товаров
    
    def should_not_be_success_message_is_disappeared_in_basket(self):
        assert self.is_disappeared(*BasketPageLocators.MESSAGES_ITEMS), \
       "Success message is presented, but should not be" # Ожидаем, что в корзине нет товаров
    def add_to_basket_home(self):
        self.browser.find_element(*BasePageLocators.ADD_TO_BASKET).click() # метод для добавления в корзину
    def should_be_basket_is_empty(self):
        # Ожидаем, что есть текст о том что корзина пуста
        assert self.is_element_present(*BasketPageLocators.CONTENT_BASKET), "basket is not empty"