import pytest
from src.prueba1 import comprobar_num


def test_comprobar_num():
    assert comprobar_num(2, 4) == 4
    assert comprobar_num(8, 2) == 8
    assert comprobar_num(20, 4) == 20
    assert comprobar_num(9, 7) ==   9
    assert comprobar_num(456, 874) == 874
    assert comprobar_num(78, 2) == 78
    assert comprobar_num(84, 84) == 0
    assert comprobar_num(2, 2) == 0
    assert comprobar_num(1250, 1250) == 0
    assert comprobar_num(45214, 45213) == 45214
