import pytest
from .pages.product_page import ProductPage


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