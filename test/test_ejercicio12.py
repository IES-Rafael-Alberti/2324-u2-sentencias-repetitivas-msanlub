from src.ejercicio12 import conteoFrase
import pytest

@pytest.mark.parametrize(
    "frase, letra,expected",
    [
    ("hola amigos","a",2),
    ("horas y horas programando","o",4),
    ("future crypto","e",1)
    ]
)

def test_conteo(frase,letra,expected):
    assert conteoFrase(frase,letra) == expected