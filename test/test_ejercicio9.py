from src.ejercicio9 import checkPassword
import pytest

@pytest.mark.parametrize(
    "passw, CONTRASEÑA, expected",
    [
    ("412","1231456",False),
    ("123456","123456",True),
    ("9558","123456",False),
        ]
)
def test_checkPassword(passw,CONTRASEÑA,expected):
    assert checkPassword(passw,CONTRASEÑA) == expected