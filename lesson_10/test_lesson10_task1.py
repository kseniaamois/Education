import allure
from selenium import webdriver
from form_page import FormPage


@allure.title("Тест заполнения формы и проверки Zip code")
@allure.description(
    "Тест проверяет заполнение формы, отправку данных, "
    "и корректность обработки поля Zip code."
)
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_form_and_validate_zip_code() -> None:
    """
    Тест открывает страницу, заполняет форму, отправляет и проверяет результат.

    Returns:
        None
    """
    driver = webdriver.Edge()
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    page = FormPage(driver)

    data = {
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job": "QA",
        "company": "SkyPro"
    }

    with allure.step("Заполнить форму данными"):
        page.fill_form(data)

    with allure.step("Отправить форму"):
        page.submit()

    with allure.step("Проверить поле Zip code"):
        zip_text = page.get_field_text("zip-code")
        zip_class = page.get_field_class("zip-code")
        with allure.step(f"Текст поля zip-code: {zip_text}"):
            assert zip_text == "N/A", "Ожидаемый текст в zip-code - 'N/A'"
        with allure.step(f"CSS класс поля zip-code: {zip_class}"):
            assert "alert-danger" in zip_class, (
                "Класс 'alert-danger' должен быть у поля Zip code"
            )

    fields = [
        ("first-name", "Иван"),
        ("last-name", "Петров"),
        ("address", "Ленина, 55-3"),
        ("e-mail", "test@skypro.com"),
        ("phone", "+7985899998787"),
        ("city", "Москва"),
        ("country", "Россия"),
        ("job-position", "QA"),
        ("company", "SkyPro"),
    ]

    with allure.step("Проверить остальные поля формы"):
        for field_id, expected_text in fields:
            text = page.get_field_text(field_id)
            css_class = page.get_field_class(field_id)
            with allure.step(f"Проверка поля '{field_id}'"):
                assert text == expected_text, (
                    f"Поле '{field_id}' содержит неожидаемый текст"
                )
                assert "alert-success" in css_class, (
                    f"Класс 'alert-success' должен быть у поля '{field_id}'"
                )

    with allure.step("Закрыть браузер"):
        driver.quit()
