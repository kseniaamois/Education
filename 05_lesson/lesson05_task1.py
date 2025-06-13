from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Если chromedriver не добавлен в PATH, укажите путь к нему:
# chromedriver_path = r"C:\path\to\chromedriver.exe"
# service = Service(executable_path=chromedriver_path)
# driver = webdriver.Chrome(service=service)

# Если chromedriver в PATH:
driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")

    # Ждём появления кнопки (по частичному совпадению класса 'btn-primary')
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
    )
    button.click()

    # Ожидаем, чтобы увидеть результат (например, появление alert)
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()

finally:
    driver.quit()
