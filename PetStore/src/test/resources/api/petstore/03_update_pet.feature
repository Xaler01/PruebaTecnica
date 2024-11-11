Feature: Update pet's name and status / Actualizar el nombre y el status de la mascota a "Sold"

Scenario: Update a pet
    Given url baseUrl + '/pet'
    And request { "id": 123, "name": "Miguelito Feliz", "status": "sold" }
    When method PUT
    Then status 200
    And print response
    And match response.name == 'Miguelito Feliz'
    And match response.status == 'sold'