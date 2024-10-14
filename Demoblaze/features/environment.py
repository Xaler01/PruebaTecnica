
import sys
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'main', 'python'))
    print(f"Project root: {project_root}")
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

def before_scenario(context, scenario):
    from pages.home_page import HomePage
    from pages.cart_page import CartPage
    context.home_page = HomePage(context.driver)
    context.cart_page = CartPage(context.driver)

@allure.step("Finalize the test execution and close the browser")
def after_all(context):
    context.driver.quit()