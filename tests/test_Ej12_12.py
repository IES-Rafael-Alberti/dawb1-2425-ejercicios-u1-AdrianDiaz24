import pytest
from src.Ej12_12 import calcular_imc

def test_calcular_imc():
    assert calcular_imc(1.90, 90) == 24.93
    assert calcular_imc(1.70, 50) == 17.30
    assert calcular_imc(1.80, 71) == 21.91
    assert calcular_imc(1.20, 32) == 22.22
    assert calcular_imc(1.45, 70) == 33.29
    assert calcular_imc(1.67, 88) == 31.55
    assert calcular_imc(1.62, 53.5) == 20.39
    assert calcular_imc(0.90, 40) == 49.38
    assert calcular_imc(2.10, 110.54) == 25.07
    assert calcular_imc(1.78, 100.21) == 31.63