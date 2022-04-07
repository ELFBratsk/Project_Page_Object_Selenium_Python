from selenium.webdriver.common.by import By
# Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject: 
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # теперь каждый селектор — это пара: как искать и что искать.
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button") # кнопка Добавить в корзину
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner .product_main > h1") # Название книги
    BASKET_ITEMS = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong") # название в корзине
    MESSAGES_ITEMS = (By.CSS_SELECTOR, "#messages .alertinner > strong") # был добавлен в вашу корзину.
    PRICE_ITEMS = (By.CSS_SELECTOR, "#content_inner .product_main .price_color") # цена книги
    PRICE_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert .alertinner  > p > strong") # цена в корзине