from src.ejercicio21 import calculoMonto,calculoDescuento
import pytest

@pytest.mark.parametrize(
    "monto, expected",
    [
    (900, 900),
    (400,400),
    (1500,1500)
        ]
)

def test_calculoMonto(monto,expected):
    assert calculoMonto(monto) == expected
    

@pytest.mark.parametrize(
    "monto, expected",
    [
    (900, 810),
    (400,360),
    (1500,1350)
        ]
)

def test_calculoDescuento(monto,expected):
    assert calculoDescuento(monto) == expected