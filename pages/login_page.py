from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
         # реализуйте проверку на корректный url адрес
         assert '/login' in self.browser.current_url, 'Не перешли по ссылке /login' 
               

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented" 
    
    #Добавьте в LoginPage метод register_new_user(email, password), который принимает две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click() # метод для регистрации
    