Feature: Servicio de Usuarios
  Scenario: procesar un usuario
    Given el servicio esta en linea
    When hago un GET a /action/1
    Then el resultado debe incluir "Hola"