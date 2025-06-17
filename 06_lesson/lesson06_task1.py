from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Нажимаем на синюю кнопку
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    wait = WebDriverWait(driver, 15)

    # Ждём появления текста в зелёной плашке
    green_box = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//p[contains(text(), 'Data loaded with AJAX get request.')]")
        )
    )

    # Кликаем по появившемуся тексту
    green_box.click()

    # Выводим текст в консоль
    print(green_box.text)  # Ожидается: Data loaded with AJAX get request.

finally:
    driver.quit()
