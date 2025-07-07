from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 90)
        self.result_locator = (By.CLASS_NAME, "screen")

    def set_delay(self, value):
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_digit(self, digit):
        btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                (
                    f"//span[contains(@class,'btn-outline-primary') and "
                    f"text()='{digit}']"
                )
            ))
        )
        btn.click()

    def click_operator(self, operator):
        btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                (
                    f"//span[contains(@class,'operator') and "
                    f"text()='{operator}']"
                )
            ))
        )
        btn.click()

    def click_equals(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                (
                    "//span[contains(@class,'btn-outline-warning') and "
                    "text()='=']"
                )
            ))
        )
        btn.click()

    def wait_for_result(self, expected_text):
        def text_to_be_exact(driver):
            element = driver.find_element(*self.result_locator)
            return element.text.strip() == expected_text
        self.wait.until(text_to_be_exact)

    def get_result(self):
        return self.driver.find_element(*self.result_locator).text.strip()
