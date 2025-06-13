from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = (
    r"C:\Users\kseni\OneDrive\Desktop\Study\pytest_course"
    r"\env_setup\DriverChrome\chromedriver.exe"
)
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Button with Dynamic ID']")
        )
    )

    button.click()

    print("Клик по кнопке выполнен успешно.", flush=True)

finally:
    driver.quit()
    print("Браузер закрыт.", flush=True)
