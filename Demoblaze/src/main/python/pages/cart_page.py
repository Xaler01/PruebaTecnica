from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_url = "https://www.demoblaze.com/cart.html"
        self.product_locator = (By.XPATH, "//tr[@class='success']//td[2]")  # Localizador de productos en la cesta
        self.place_order_button = (By.XPATH, "//button[text()='Place Order']")

    def open_cart(self):
        self.driver.get(self.cart_url)

    def get_products_in_cart(self):
        """Recupera los nombres de los productos del carrito."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.product_locator))
        products = self.driver.find_elements(*self.product_locator)
        return [product.text for product in products]

    def verify_product_in_cart(self, product_name):
        """Verificar si un producto específico está en el carrito."""
        products = self.get_products_in_cart()
        return product_name in products

    def click_place_order(self):
        """Clic en el botón 'Place Order' para proceder a la compra."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.place_order_button)).click()

    def complete_purchase(self, name, country, city, credit_card, month, year):
        """Llenar el formulario de compra y enviar."""
        self.click_place_order()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))

        # Llenar el formulario
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(credit_card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)

        # Envíar el formulario
        self.driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

    def get_confirmation_message(self):
        """Recibir el mensaje de confirmación después de una compra exitosa."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sweet-alert h2")))
        return self.driver.find_element(By.CSS_SELECTOR, ".sweet-alert h2").text
