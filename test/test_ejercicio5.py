from src.ejercicio5 import calculoCapital
import pytest

@pytest.mark.parametrize(
    "cantidad, interes, años, expected",
    [
        (2,3,2,[2.06, 2.1218]),
        (1500,3,4,[1545.0, 1591.3500000000001, 1639.0905000000002, 1688.2632150000004])
    ]
)

def test_calculoCapital(cantidad,interes,años,expected):
    assert calculoCapital(cantidad,interes,años) == expected