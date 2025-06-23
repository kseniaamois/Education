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

    # Ждем, когда в зеленой плашке появится нужный текст
    green_box = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "bg-success"),
            "Data loaded with AJAX get request."
        )
    )

    # Получаем сам элемент и его текст
    green_box_elem = driver.find_element(By.CLASS_NAME, "bg-success")
    print(green_box_elem.text)

finally:
    driver.quit()
