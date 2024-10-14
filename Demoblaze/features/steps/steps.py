from behave import given, when, then
from pages.home_page import HomePage
from pages.cart_page import CartPage
import time
import allure

@given('I am on the DemoBlaze homepage')
@allure.step("Abrir la página de inicio de DemoBlaze")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.open()

@when('I add "{product}" to the cart')
@allure.step("Añadir {product} al carrito")
def step_impl(context, product):
    context.home_page.select_product(product)
    context.home_page.click_add_to_cart()
    context.home_page.accept_alert()
    context.home_page.return_to_homepage()

@then('I should see the cart with the added products')
@allure.step("Comprobar que el carrito contiene los productos ")
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    context.home_page.view_cart()
    time.sleep(2)

@when('I complete the purchase with valid details')
@allure.step("Completar el formulario con datos válidos")
def step_impl(context):
    context.cart_page.complete_purchase(
        name="Alexander",
        country="Ecuador",
        city="Quito",
        credit_card="ABCD EFGH IJKL MNOP",
        month="12",
        year="2024"
    )
    time.sleep(2)

@then('I should see a confirmation message')
@allure.step("Comprobar mensaje de confirmación de la compra")
def step_impl(context):
    confirmation_message = context.cart_page.get_confirmation_message()
    assert confirmation_message == "Thank you for your purchase!", f"Expected confirmation message not found: {confirmation_message}"
