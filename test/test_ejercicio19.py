from src.ejercicio19 import eligeMenu
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
    ("1", "Este es el texto que se imprime con la opción 1"),
    ("2","Este es el texto que se imprime con la opción 2"),
    ("9","Error,vuelva a indicar una opción correcta."),
    ("3","Programa finalizado")
        ]
)

def test_eligeMenu(numero,expected):
    assert eligeMenu(numero) == expected