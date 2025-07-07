from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        # Кнопка "Add to cart" для товара по его названию
        self.driver.find_element(
            By.XPATH,
            (
                f"//div[text()='{product_name}']"
                "/ancestor::div[@class='inventory_item']//button"
            )
        ).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
