from src.ejercicio4 import listaEntero
import pytest

@pytest.mark.parametrize(
    "entero, expected",
    [
    (5,[5,4,3,2,1,0]),
     (3,[3,2,1,0]),
     (2,[2,1,0]),
        ]
)

def test_listaEntero(entero,expected):
    assert listaEntero(entero) == expected