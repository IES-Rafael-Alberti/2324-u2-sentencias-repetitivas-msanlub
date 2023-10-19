from src.ejercicio8 import calculoTriangulo
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
    (6,"1\n31\n531\n"),
    (10,"1\n31\n531\n7531\n97531\n"),
    (4,"1\n31\n")
    ]
)

def test_calculoTriangulo(numero,expected):
    assert calculoTriangulo(numero) == expected