from src.ejercicio1 import repetirPalabra
import pytest

@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("hola",  "hola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\n"),
        ]
)

def test_repetirPalabra(palabra,expected):
    assert repetirPalabra(palabra) == expected