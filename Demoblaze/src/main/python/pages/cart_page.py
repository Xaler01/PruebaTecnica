from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_url = "https://www.demoblaze.com/cart.html"
        self.product_locator = (By.XPATH, "//tr[@class='success']//td[2]")  # Locator for products in the cart
        self.place_order_button = (By.XPATH, "//button[text()='Place Order']")

    def open_cart(self):

        self.driver.get(self.cart_url)

    def get_products_in_cart(self):
        """Retrieve the names of products in the cart."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_locator)
        )
        products = self.driver.find_elements(*self.product_locator)
        return [product.text for product in products]

    def verify_product_in_cart(self, product_name):
        """Verify if a specific product is in the cart."""
        products = self.get_products_in_cart()
        return product_name in products

    def click_place_order(self):
        """Click the 'Place Order' button to proceed with purchase."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.place_order_button)
        ).click()

    def complete_purchase(self, name, country, city, credit_card, month, year):
        """Fill out the purchase form and submit it."""
        self.click_place_order()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))

        # Fill out the form
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(credit_card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)

        # Submit the form
        self.driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

    def get_confirmation_message(self):
        """Get the confirmation message after a successful purchase."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".sweet-alert h2"))
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".sweet-alert h2").text