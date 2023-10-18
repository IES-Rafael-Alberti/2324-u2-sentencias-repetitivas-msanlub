from src.ejercicio2 import repetirEdad
import pytest

@pytest.mark.parametrize(
    "edad, expected",
    [
    (5,[1,2,3,4,5]),
    (3,[1,2,3]),
    (2,[1,2]),
        ]
)

def test_repetirEdad(edad,expected):
    assert repetirEdad(edad) == expected