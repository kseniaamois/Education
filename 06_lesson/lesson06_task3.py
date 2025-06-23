from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 30)

    # Ждем, пока элемент с id="award" появится в DOM
    wait.until(lambda d: d.find_element(By.ID, "award"))

    # Ждем, пока картинка полностью загрузится (complete == true)
    wait.until(lambda d: d.execute_script(
        "return document.getElementById('award').complete && document.getElementById('award').naturalWidth > 0;"
    ))

    award_img = driver.find_element(By.ID, "award")
    src_value = award_img.get_attribute("src")
    print(src_value)

finally:
    driver.quit()
