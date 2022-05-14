# Project_Page_Object_Selenium_Python

Итоговое тестовое задание от STEPIKпо Автоматизация
тестирования с помощью Selenium и Python
Версия Python 3.9.5
Дополнительные модули:
atomicwrites==1.4.0
attrs==21.4.0
colorama==0.4.4
iniconfig==1.1.1
packaging==21.3
pluggy==0.13.1
py==1.11.0
pyparsing==3.0.8
pytest==7.1.1
selenium==3.14.0
tomli==2.0.1
urllib3==1.26.9

Все тесты, описанные в test_main_page.py и test_product_page.py запускаются и проходят.

Маркированные тесты запускаются успешно:

pytest -v --tb=line --language=en -m need_review

Все тесты написаны в стиле PageObject: нет assert в теле
тестов, все методы действия и проверки выделены в отдельные методы в классах
PageObject, все селекторы лежат в locators.py
