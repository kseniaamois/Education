from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

geckodriver_path = (
    r"C:\Users\kseni\OneDrive\Desktop\Study\pytest_course"
    r"\env_setup\DriverFireFox\geckodriver.exe"
)
service = Service(executable_path=geckodriver_path)

driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "input")
        )
    )

    input_field.send_keys("Sky")
    input_field.clear()
    input_field.send_keys("Pro")

    print(
        "Текст 'Sky' и 'Pro' успешно введён в поле.",
        flush=True
    )

finally:
    driver.quit()
    print("Браузер закрыт.", flush=True)
