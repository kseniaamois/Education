# Автотесты интернет-магазина saucedemo.com

## Описание проекта

Этот проект содержит автоматизированные тесты для проверки 
функциональности интернет-магазина  
[https://www.saucedemo.com/](https://www.saucedemo.com/) 
с использованием паттерна Page Object и Selenium WebDriver на Python.

---

## Как запустить тесты для формирования отчета

1. Убедитесь, что у вас установлены необходимые библиотеки:

`pip install selenium pytest allure-pytest`

2. Запустите тесты командой:

- Если в вашем проекте **есть** файл `pytest.ini` с нужными настройками (например, `--alluredir=allure-results`), то просто выполните:

`pytest`

- Если **файла `pytest.ini` нет**, то обязательно укажите путь для сохранения отчетов вручную:

`pytest --alluredir=allure-results`

> Рекомендуется создать файл `pytest.ini` в корне проекта с таким содержимым:

[pytest]
addopts = --alluredir=allure-results
testpaths = tests

> Это позволит запускать тесты командой `pytest` без дополнительных параметров.

---

## Как просмотреть сформированный отчет

1. Установите Allure Commandline согласно официальной инструкции:  
[https://docs.qameta.io/allure/#_installing_a_commandline](https://docs.qameta.io/allure/#_installing_a_commandline)

2. После выполнения тестов запустите команду:

`allure serve allure-results`

> Она откроет локальный веб-сервер с подробным визуальным отчетом тестирования.