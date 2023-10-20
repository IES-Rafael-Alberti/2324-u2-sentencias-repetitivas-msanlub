from src.ejercicio15 import listaNumeros
import pytest

@pytest.mark.parametrize(
    "numero,expected",
    [
    (),
    (),
    ()
    ]
)

def test_listaNumeros(numero,expected):
    assert listaNumeros(numero) == expected