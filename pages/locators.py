from selenium.webdriver.common.by import By
# Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject: 
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # теперь каждый селектор — это пара: как искать и что искать.
    
class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_link")
    