from src.ejercicio16 import listaNumeros
import pytest

@pytest.mark.parametrize(
    "numero,expected",
    [
    (6,6),
    (3,9),
    (55,932)
    ]
)

def test_listaNumeros(numero,expected):
    assert listaNumeros(numero) == expected