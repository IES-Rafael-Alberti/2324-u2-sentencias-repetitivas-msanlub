from src.ejercicio6 import calculoTriangulo
import pytest

@pytest.mark.parametrize(
    "numero, expected",
    [
        (5,['*', '**', '***', '****', '*****']),
        (2,['*', '**']),
        (9,['*', '**', '***', '****', '*****', '******', '*******', '********', '*********'])
    ]
)

def test_calculoTriangulo(numero,expected):
    assert calculoTriangulo(numero) == expected