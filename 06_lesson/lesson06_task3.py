from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    wait = WebDriverWait(driver, 30)

    # Ждём, пока в DOM появится минимум 3 картинки
    wait.until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
    )

    # Ждём, пока все картинки будут полностью загружены (complete == true)
    wait.until(
        lambda d: d.execute_script(
            'return Array.from(document.images).every(img => img.complete);'
        )
    )

    images = driver.find_elements(By.TAG_NAME, "img")

    # Получаем src третьей картинки (индекс 2)
    src_value = images[2].get_attribute("src")
    print(src_value)

finally:
    driver.quit()
