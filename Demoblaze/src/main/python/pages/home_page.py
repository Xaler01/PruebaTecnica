
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demoblaze.com"
        self.samsung_galaxy_s6_link = (By.LINK_TEXT, "Samsung galaxy s6")
        self.add_to_cart_button = (By.XPATH, "//a[text()='Add to cart']")
        self.cart_link = (By.ID, "cartur")

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.samsung_galaxy_s6_link))

    def select_product(self, product_name):
        product_link = (By.LINK_TEXT, product_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(product_link)).click()

    def click_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.add_to_cart_button)).click()

    def accept_alert(self):
        WebDriverWait(self.driver, 20).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def return_to_homepage(self):
        self.driver.get(self.url)

    def view_cart(self):
        self.driver.find_element(*self.cart_link).click()