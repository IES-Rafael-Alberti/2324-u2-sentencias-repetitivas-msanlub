from src.ejercicio13 import ecoFrase
import pytest

@pytest.mark.parametrize(
    "frase,expected",
    [
    ("salir",False),
    ("horas y horas programando",True),
    ("future crypto",True)
    ]
)

def test_eco(frase,expected):
    assert ecoFrase(frase) == expected