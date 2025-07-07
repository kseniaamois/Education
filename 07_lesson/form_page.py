from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SUBMIT_BTN = "button[type='submit']"


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_form(self, data):
        self.driver.find_element(
            By.NAME, "first-name"
        ).send_keys(data["first_name"])
        self.driver.find_element(
            By.NAME, "last-name"
        ).send_keys(data["last_name"])
        self.driver.find_element(
            By.NAME, "address"
        ).send_keys(data["address"])
        self.driver.find_element(
            By.NAME, "e-mail"
        ).send_keys(data["email"])
        self.driver.find_element(
            By.NAME, "phone"
        ).send_keys(data["phone"])
        # Zip code не заполняем
        self.driver.find_element(
            By.NAME, "city"
        ).send_keys(data["city"])
        self.driver.find_element(
            By.NAME, "country"
        ).send_keys(data["country"])
        self.driver.find_element(
            By.NAME, "job-position"
        ).send_keys(data["job"])
        self.driver.find_element(
            By.NAME, "company"
        ).send_keys(data["company"])

    def submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, SUBMIT_BTN
        ).click()

    def get_field_text(self, field_id):
        elem = self.wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        return elem.text

    def get_field_class(self, field_id):
        elem = self.wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        return elem.get_attribute("class")
