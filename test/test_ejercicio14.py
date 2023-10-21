'''from src.ejercicio14 import listaNumeros
import pytest

@pytest.mark.parametrize(
    "numero,expected",
    [
    ([6,6],12),
    ([20,5],25),
    ([92,5],97)
    ]
)

def test_lista_numeros(numero,expected):
    assert listaNumeros(numero) == expected'''