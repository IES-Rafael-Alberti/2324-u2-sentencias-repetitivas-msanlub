from src.ejercicio3 import numeroImpar
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
        (5,[1,3]),
        (2,[1]),
        (9,[1,3,5,7])
    ]
)

def test_numeroImpar(numero,expected):
    assert numeroImpar(numero) == expected