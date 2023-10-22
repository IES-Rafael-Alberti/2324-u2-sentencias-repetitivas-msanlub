from src.ejercicio22 import numeroParidad
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
    (254,False),
    (44,False),
    (253,True),
    (9,True)
        ]
)

def test_numeroParidad(numero,expected):
    assert numeroParidad(numero) == expected