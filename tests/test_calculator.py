# tests/test_calculator.py
from calculator import calc

def test_add():
    assert calc(3,2,"+") == 5

def test_div_zero():
    assert calc(5,0,"/") == "inf"

def test_mul():
    assert calc(4,2,"*") == 8
