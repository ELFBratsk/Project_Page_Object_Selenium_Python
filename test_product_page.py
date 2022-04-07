from .pages.main_page import MainPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
        
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор      экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_basket()          # метод для добавления в корзину
    page.solve_quiz_and_get_code() # результат математического выражения и ввести ответ
    

def test_guest_should_see_login_link(browser):
    
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

