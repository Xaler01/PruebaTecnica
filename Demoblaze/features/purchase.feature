# Feature: Purchase Products - Funcionalidad para realizar la compra de productos
# Este archivo define el flujo de pruebas para añadir productos al carrito y completar la compra en Demoblaze.
#Funcion Comprar Productos
Feature: Purchase Products

   Scenario: Añadir productos al carrito y completar la compra

        #Dado que Estoy en la página de inicio de DemoBlaze
        Given I am on the DemoBlaze homepage

        # Añadir productos específicos al carrito
        #Cuando Añado Samsung galaxy s6 al carrito
        When I add "Samsung galaxy s6" to the cart
        #y Añado Sony xperia z5 al carrito
        And I add "Sony xperia z5" to the cart

        #Entonces debería ver el carrito con los productos añadidos
        Then I should see the cart with the added products

        #Cuando Complete la compra con datos válidos
        When I complete the purchase with valid details

        #Entonces debería ver un mensaje de confirmación
        Then I should see a confirmation message

