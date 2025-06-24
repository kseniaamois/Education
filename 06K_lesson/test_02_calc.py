from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def text_to_be_exact(locator, text):
    def _predicate(driver):
        element = driver.find_element(*locator)
        return element.text.strip() == text
    return _predicate


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    wait = WebDriverWait(driver, 90)

    try:
        delay_input = wait.until(
            EC.presence_of_element_located(
                (By.ID, "delay")
            )
        )
        delay_input.clear()
        delay_input.send_keys("45")

        btn_7 = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    (
                        "//span[contains(@class,'btn-outline-primary') and "
                        "text()='7']"
                    )
                )
            )
        )
        btn_plus = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    (
                        "//span[contains(@class,'operator') and "
                        "text()='+']"
                    )
                )
            )
        )
        btn_8 = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    (
                        "//span[contains(@class,'btn-outline-primary') and "
                        "text()='8']"
                    )
                )
            )
        )
        btn_equals = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    (
                        "//span[contains(@class,'btn-outline-warning') and "
                        "text()='=']"
                    )
                )
            )
        )

        btn_7.click()
        btn_plus.click()
        btn_8.click()
        btn_equals.click()

        result_locator = (By.CLASS_NAME, "screen")
        wait.until(text_to_be_exact(result_locator, "15"))

        result_elem = driver.find_element(*result_locator)
        result_text = result_elem.text.strip()
        assert result_text == "15", (
            f"Ожидали результат 15, получили {result_text}"
        )

    finally:
        driver.quit()
