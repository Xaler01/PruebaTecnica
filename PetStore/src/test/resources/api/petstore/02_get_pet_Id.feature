Feature: Previously entered pet / Consultar la mascota ingresada previamente.

  Scenario: Get pet by ID
    Given url 'https://petstore.swagger.io/v2/pet/123'
    When method GET
    Then status 200
    And print response
    And match response.id == 123