from typing import Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SUBMIT_BTN = "button[type='submit']"


class FormPage:
    """
    PageObject класс для страницы с формой.

    Args:
        driver (WebDriver): экземпляр драйвера Selenium.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация PageObject.

        Args:
            driver (WebDriver): браузерный драйвер.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_form(self, data: Dict[str, str]) -> None:
        """
        Заполняет форму данными из словаря.

        Args:
            data (Dict[str, str]): словарь с данными для полей формы,
                ключи соответствуют атрибуту name элементов.
        """
        self.driver.find_element(By.NAME, "first-name").send_keys(
            data["first_name"]
        )
        self.driver.find_element(By.NAME, "last-name").send_keys(
            data["last_name"]
        )
        self.driver.find_element(By.NAME, "address").send_keys(
            data["address"]
        )
        self.driver.find_element(By.NAME, "e-mail").send_keys(
            data["email"]
        )
        self.driver.find_element(By.NAME, "phone").send_keys(
            data["phone"]
        )
        # Zip code не заполняется намеренно
        self.driver.find_element(By.NAME, "city").send_keys(
            data["city"]
        )
        self.driver.find_element(By.NAME, "country").send_keys(
            data["country"]
        )
        self.driver.find_element(By.NAME, "job-position").send_keys(
            data["job"]
        )
        self.driver.find_element(By.NAME, "company").send_keys(
            data["company"]
        )

    def submit(self) -> None:
        """
        Нажимает кнопку отправки формы.
        """
        self.driver.find_element(By.CSS_SELECTOR, SUBMIT_BTN).click()

    def get_field_text(self, field_id: str) -> str:
        """
        Получает текст из элемента по указанному ID.

        Args:
            field_id (str): атрибут id HTML-элемента.

        Returns:
            str: текстовое содержимое элемента.
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        return element.text

    def get_field_class(self, field_id: str) -> str:
        """
        Получает значение атрибута 'class' указанного элемента по ID.

        Args:
            field_id (str): атрибут id HTML-элемента.

        Returns:
            str: строка с классами элемента.
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        return element.get_attribute("class")
