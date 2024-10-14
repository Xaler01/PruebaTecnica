Feature: Purchase Products
    Scenario: Añadir productos al carrito y completar la compra
        Given I am on the DemoBlaze homepage
        When I add "Samsung galaxy s6" to the cart
        And I add "Sony xperia z5" to the cart
        And I add "Iphone 6 32gb" to the cart
        Then I should see the cart with the added products
        When I complete the purchase with valid details
        Then I should see a confirmation message