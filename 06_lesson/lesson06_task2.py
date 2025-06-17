from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода и вводим текст "SkyPro" с помощью send_keys
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()
    input_field.send_keys("SkyPro")

    # Нажимаем на синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Ждём, что текст кнопки изменится на "SkyPro"
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "updatingButton"),
            "SkyPro"
        )
    )

    # Получаем текст кнопки и выводим в консоль
    print(button.text)  # Ожидается: SkyPro

finally:
    driver.quit()
