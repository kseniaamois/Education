from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    PageObject класс для страницы авторизации.

    Args:
        driver (WebDriver): экземпляр selenium WebDriver.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        Args:
            driver (WebDriver): браузерный драйвер.
        """
        self.driver = driver

    def enter_username(self, username: str) -> None:
        """
        Ввести имя пользователя.

        Args:
            username (str): имя пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввести пароль.

        Args:
            password (str): пароль пользователя.
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self) -> None:
        """
        Кликнуть кнопку входа.
        """
        self.driver.find_element(By.ID, "login-button").click()
