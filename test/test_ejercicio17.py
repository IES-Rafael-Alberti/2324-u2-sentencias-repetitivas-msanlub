from src.ejercicio17 import separar
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
    (1045,10),
    (50,5),
    (2345,14),
        ]
)

def test_separar(numero,expected):
    assert separar(numero) == expected