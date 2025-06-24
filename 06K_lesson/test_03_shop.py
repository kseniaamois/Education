from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CART_CLS = "shopping_cart_link"


def test_shop_total():
    driver = webdriver.Firefox()
    url = "https://www.saucedemo.com/"
    driver.get(url)
    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        wait = WebDriverWait(driver, 10)

        backpack_id = "add-to-cart-sauce-labs-backpack"
        driver.find_element(By.ID, backpack_id).click()

        bolt_tshirt_id = "add-to-cart-sauce-labs-bolt-t-shirt"
        driver.find_element(By.ID, bolt_tshirt_id).click()

        onesie_id = "add-to-cart-sauce-labs-onesie"
        driver.find_element(By.ID, onesie_id).click()

        cart_link = driver.find_element(By.CLASS_NAME, CART_CLS)
        cart_link.click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Ksenia")
        driver.find_element(By.ID, "last-name").send_keys("Amoiseeva")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        locator = (By.CLASS_NAME, "summary_total_label")
        total = wait.until(EC.presence_of_element_located(locator)).text
        assert "$58.29" in total
    finally:
        driver.quit()
