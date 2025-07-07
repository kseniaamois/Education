from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    page = CalculatorPage(driver)

    page.set_delay(45)
    page.click_digit("7")
    page.click_operator("+")
    page.click_digit("8")
    page.click_equals()
    page.wait_for_result("15")

    result_text = page.get_result()
    assert result_text == "15", (
        f"Ожидали результат 15, получили {result_text}"
    )

    driver.quit()
