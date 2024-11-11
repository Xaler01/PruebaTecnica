Feature: Add a new pet to the store / Anadir una mascota a la tienda

Scenario: Add a pet
    Given url baseUrl + '/pet'
    And request { "id": 123, "name": "Miguelito", "status": "available" }
    When method POST
    Then status 200
    And print response
    And match response.id == 123
    And match response.name == 'Miguelito'
    And match response.status == 'available'

