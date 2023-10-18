from src.ejercicio5 import calculoCapital
import pytest

@pytest.mark.parametrize(
    "cantidad, interes, años, expected",
    [
    (2,3,2,"En el año 1 el capital es: 2.06","En el año 2 el capital es: 2.12"),
       ]
)

def test_calculoCapital(cantidad,interes,años,expected):
    assert calculoCapital(cantidad,interes,años) == expected