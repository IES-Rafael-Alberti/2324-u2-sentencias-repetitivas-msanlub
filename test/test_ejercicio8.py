from src.ejercicio8 import calculoTriangulo
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
    (6,[1], [3,1],[5,3,1]),
    
        ]
)

def test_calculoTriangulo(numero,expected):
    assert calculoTriangulo(numero) == expected