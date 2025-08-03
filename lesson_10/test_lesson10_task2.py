import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.title("Тест калькулятора с задержкой на slow-calculator.html")
@allure.description(
    "Проверяет корректность выполнения операции сложения с задержкой "
    "в калькуляторе."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator() -> None:
    """
    Тест открывает страницу калькулятора, задаёт задержку, вводит
    выражение 7 + 8, ждёт результат и проверяет вывод.

    Returns:
        None
    """
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    page = CalculatorPage(driver)

    with allure.step("Установить задержку вычисления в 45 секунд"):
        page.set_delay(45)

    with allure.step("Нажать кнопку '7'"):
        page.click_digit("7")

    with allure.step("Нажать оператор '+'"):
        page.click_operator("+")

    with allure.step("Нажать кнопку '8'"):
        page.click_digit("8")

    with allure.step("Нажать кнопку '=' (равно)"):
        page.click_equals()

    with allure.step("Ожидать появления результата '15'"):
        page.wait_for_result("15")

    with allure.step("Проверить корректность результата"):
        result_text = page.get_result()
        assert result_text == "15", (
            f"Ожидали результат 15, получили {result_text}"
        )

    with allure.step("Закрыть браузер"):
        driver.quit()
