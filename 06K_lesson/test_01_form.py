from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SUBMIT_BTN = "button[type='submit']"


def test_fill_form_and_validate_zip_code():
    driver = webdriver.Edge()
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    wait = WebDriverWait(driver, 20)

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Оставляем Zip code пустым для проверки ошибки
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(
        By.CSS_SELECTOR,
        SUBMIT_BTN
    ).click()

    # Проверяем, что Zip code подсвечен красным и содержит 'N/A'
    zip_code_div = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )
    assert zip_code_div.text == "N/A"
    assert "alert-danger" in zip_code_div.get_attribute("class")

    # Проверяем остальные поля на зелёную подсветку
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
        elem = wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        assert elem.text == expected_text
        assert "alert-success" in elem.get_attribute("class")

    driver.quit()
