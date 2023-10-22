from src.ejercicio10 import numPrimo
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
    (5,True),
    (12,False),
    (9,False),
    (5,True)
        ]
)

def test_numPrimo(numero,expected):
    assert numPrimo(numero) == expected