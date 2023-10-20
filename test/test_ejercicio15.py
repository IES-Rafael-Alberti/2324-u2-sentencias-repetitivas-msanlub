from src.ejercicio15 import suma
import pytest

@pytest.mark.parametrize(
    "numero,expected",
    [
    (),
    (),
    ()
    ]
)

def test_suma(numero,expected):
    assert suma(numero) == expected