@titulo
Feature: Buscador de libros

    Scenario: Buscador de libros
        Given que ingrese en la web de la Biblioteca de Soria
        When realizo la busqueda de "Numancia"
        Then compruebo los resultados

    