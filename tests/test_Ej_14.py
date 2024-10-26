import pytest
from src.Ej12_14 import calcular_peso

def test_calcular_imc():
    assert calcular_peso(100, 90) == 17950
    assert calcular_peso(1, 50) == 3862
    assert calcular_peso(20, 71) == 7565
    assert calcular_peso(14, 32) == 3968
    assert calcular_peso(54, 70) == 11298
    assert calcular_peso(140, 88) == 22280
    assert calcular_peso(24, 53) == 6663
    assert calcular_peso(90, 40) == 13080
    assert calcular_peso(1000, 110) == 120250
    assert calcular_peso(178, 100) == 27436