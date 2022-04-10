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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert-success") # сообщение об успешном добавлении в корзину (по селектору их 3)

# В файле locators.py создаем новый класс BasePageLocators и переносим туда соответствующие элементы:
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link") # изначально был селектор #login_link_ink (и был не верен)
    BASKET_BTN = (By.CSS_SELECTOR, "#default .btn-group a.btn.btn-default ") # кнопка корзины
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > section > div > ol > li:nth-child(1) > article > div.product_price > form > button") # кнопка Добавить в корзину (это ято бы проверить тесты 4.3.10 не очень хороший селектор)
    
# Локаторы BasketPageLocators для страницы корзины    
class BasketPageLocators():
    MESSAGES_ITEMS = (By.CSS_SELECTOR, "#messages .alertinner > strong") # Информация о товаре если в корзине присутствует товар.
    CONTENT_BASKET = (By.CSS_SELECTOR, "#content_inner > p > a") # Ваша корзина пуста