from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name(self, value):
        self.driver.find_element(By.ID, "first-name").send_keys(value)

    def fill_last_name(self, value):
        self.driver.find_element(By.ID, "last-name").send_keys(value)

    def fill_postal_code(self, value):
        self.driver.find_element(By.ID, "postal-code").send_keys(value)

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        # Ожидаем появления суммы Total
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text
        # Пример: "Total: $58.29" → $58.29
        return total_text.split("$")[-1]
