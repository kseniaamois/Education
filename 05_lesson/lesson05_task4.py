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
    driver.get("http://the-internet.herokuapp.com/login")

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "username")
        )
    )
    username_input.send_keys("tomsmith")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.flash.success")
        )
    )
    print(
        success_message.text.strip(),
        flush=True
    )

finally:
    driver.quit()
    print("Браузер закрыт.", flush=True)
