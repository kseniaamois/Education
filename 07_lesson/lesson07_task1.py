from selenium import webdriver
from form_page import FormPage


def test_fill_form_and_validate_zip_code():
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

    page.fill_form(data)
    page.submit()

    # Проверяем Zip code
    zip_text = page.get_field_text("zip-code")
    zip_class = page.get_field_class("zip-code")
    assert zip_text == "N/A"
    assert "alert-danger" in zip_class

    # Проверяем остальные поля
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

    for field_id, expected_text in fields:
        text = page.get_field_text(field_id)
        css_class = page.get_field_class(field_id)
        assert text == expected_text
        assert "alert-success" in css_class

    driver.quit()
