import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Чтобы указать язык браузера с помощью WebDriver, используйте класс Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, es and td.')


@pytest.fixture(scope="function") #Браузер должен объявляться в фикстуре browser
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options() #используйте класс Options
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) #метод add_experimental_option
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile() #используйте класс FirefoxProfile
        fp.set_preference("intl.accept_languages", user_language) #метод set_preference
        browser = webdriver.Firefox(firefox_profile=fp)
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()