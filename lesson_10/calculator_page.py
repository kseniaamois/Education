from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    PageObject класс для страницы калькулятора slow-calculator.html.

    Args:
        driver (WebDriver): экземпляр веб-драйвера Selenium.
    """

    def __init__(self, driver: WebDriver, wait_timeout: int = 90) -> None:
        """
        Инициализация PageObject.

        Args:
            driver (WebDriver): Selenium WebDriver.
            wait_timeout (int): Максимальное время ожидания элементов.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.result_locator = (By.CLASS_NAME, "screen")

    def set_delay(self, value: int) -> None:
        """
        Установить задержку вычисления калькулятора.

        Args:
            value (int): значение задержки в секундах.
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_digit(self, digit: str) -> None:
        """
        Нажать кнопку цифры.

        Args:
            digit (str): символ цифры (например, "7").
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//span[contains(@class,'btn-outline-primary') and "
                    f"text()='{digit}']",
                )
            )
        )
        btn.click()

    def click_operator(self, operator: str) -> None:
        """
        Нажать кнопку оператора.

        Args:
            operator (str): символ оператора (например, "+").
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//span[contains(@class,'operator') and "
                    f"text()='{operator}']",
                )
            )
        )
        btn.click()

    def click_equals(self) -> None:
        """
        Нажать кнопку "=".
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[contains(@class,'btn-outline-warning') and "
                    "text()='=']",
                )
            )
        )
        btn.click()

    def wait_for_result(
        self, expected_text: str, timeout: Optional[int] = None
    ) -> None:
        """
        Ожидать появления ожидаемого результата на экране калькулятора.

        Args:
            expected_text (str): ожидаемый результат.
            timeout (Optional[int]): время ожидания в секундах
                (по умолчанию self.wait.timeout).
        """
        wait_obj = self.wait
        if timeout is not None:
            wait_obj = WebDriverWait(self.driver, timeout)

        def text_to_be_exact(driver: WebDriver) -> bool:
            element = driver.find_element(*self.result_locator)
            return element.text.strip() == expected_text

        wait_obj.until(text_to_be_exact)

    def get_result(self) -> str:
        """
        Получить текущий результат с экрана калькулятора.

        Returns:
            str: текст результата.
        """
        return self.driver.find_element(*self.result_locator).text.strip()
