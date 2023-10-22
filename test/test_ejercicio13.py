from src.ejercicio13 import fraseSalida
import pytest

@pytest.mark.parametrize(
    "frase,FIN,expected",
    [
    ("salir","salir",True),
    ("horas y horas programando","salir",False),
    ("future crypto","salir",False)
    ]
)

def test_fraseSalida(frase,FIN,expected):
    assert fraseSalida(frase,FIN) == expected