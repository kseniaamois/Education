from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class CartPage:
    """
    PageObject класс для страницы корзины.

    Args:
        driver (WebDriver): экземпляр selenium WebDriver.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        Args:
            driver (WebDriver): браузерный драйвер.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд

    def click_checkout(self) -> None:
        """
        Нажать кнопку оформления заказа.
        """
        # Явное ожидание кликабельности кнопки
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        self.driver.find_element(By.ID, "checkout").click()

    def get_cart_items(self) -> List[str]:
        """
        Получить список названий товаров в корзине.

        Returns:
            List[str]: список названий товаров.
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]
