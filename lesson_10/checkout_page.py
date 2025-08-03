from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    PageObject класс для страницы оформления заказа.

    Args:
        driver (WebDriver): экземпляр selenium WebDriver.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver (WebDriver): браузерный драйвер.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name(self, value: str) -> None:
        """
        Заполнить поле имени.

        Args:
            value (str): имя.
        """
        first_name_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_input.clear()
        first_name_input.send_keys(value)

    def fill_last_name(self, value: str) -> None:
        """
        Заполнить поле фамилии.

        Args:
            value (str): фамилия.
        """
        last_name_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        )
        last_name_input.clear()
        last_name_input.send_keys(value)

    def fill_postal_code(self, value: str) -> None:
        """
        Заполнить поле почтового индекса.

        Args:
            value (str): почтовый индекс.
        """
        postal_code_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        )
        postal_code_input.clear()
        postal_code_input.send_keys(value)

    def click_continue(self) -> None:
        """
        Нажать кнопку продолжения оформления.
        """
        continue_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

    def get_total(self) -> str:
        """
        Получить итоговую сумму заказа.

        Returns:
            str: строка с суммой, например "58.29".
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text
        # Пример: "Total: $58.29" → "58.29"
        total_value = total_text.split("$")[-1].strip()
        return total_value
