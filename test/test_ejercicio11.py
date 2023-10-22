from src.ejercicio11 import palabraInvertida
import pytest

@pytest.mark.parametrize(
    "palabra, expected",
    [
    ("hola", "aloh"),
    ("rafa","afar")
        ]
)

def test_palabraInvertida(palabra,expected):
    assert palabraInvertida(palabra) == expected