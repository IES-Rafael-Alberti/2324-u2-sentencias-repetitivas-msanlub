from src.ejercicio14 import suma
import pytest

@pytest.mark.parametrize(
    "numero,expected",
    [
    (6,),
    (3,),
    (55,)
    ]
)

def test_suma(numero,expected):
    assert suma(numero) == expected