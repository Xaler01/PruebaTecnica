Feature: Get pets by status / Consultar la mascota modificada por estatus

@EjecutarEscenario
Scenario: Retrieve pets by status "sold"
    Given url 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
    When method GET
    Then status 200
    And print response
    And match response[0].status == 'sold'