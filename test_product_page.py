import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
link4_3_2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear" 
link4_3_3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('link', [link4_3_2,link4_3_3])
def test_guest_can_add_product_to_basket(browser, link):
    
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор      экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_basket()          # метод для добавления в корзину
    page.solve_quiz_and_get_code() # результат математического выражения и ввести ответ
    page.should_to_basket() # делаем проверку

@pytest.mark.parametrize('link', [0,1,2,3,4,5,6,pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),8,9])
def test_guest_can_add_product_to_basket_promo(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор      экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_basket()          # метод для добавления в корзину
    page.solve_quiz_and_get_code() # результат математического выражения и ввести ответ
    page.should_to_basket() # делаем проверку 

@pytest.mark.xfail # Добавим маркировку @pytest.mark.xfail для падающего теста
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()          # метод для добавления в корзину
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail # Добавим маркировку @pytest.mark.xfail для падающего теста
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()          # метод для добавления в корзину
    page.should_not_be_success_message_is_disappeared() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present



# Теперь мы можем легко добавлять тесты вида "гость может перейти на страницу логина со страницы Х".     
def test_guest_should_see_login_link_on_product_page(browser):
    link1 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link1)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_login_page()