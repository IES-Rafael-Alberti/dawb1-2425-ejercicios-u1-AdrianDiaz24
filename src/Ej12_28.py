# Calcular el área de un triángulo a partir de tres lados


def calcular_area(lado_a, lado_b, lado_c):
    semiperimetro = ((lado_a+lado_b+lado_c)/2)
    import math
    area = math.sqrt(semiperimetro*((semiperimetro-lado_a)*(semiperimetro-lado_b)*(semiperimetro-lado_c)))
    area = round(area,2)
    return area


def main():
    lado_a = float(input("Dame la longitud del 1º lado del triangulo: "))
    lado_b = float(input("Dame la longitud del 2º lado del triangulo: "))
    lado_c = float(input("Dame la longitud del 3º lado del triangulo: "))

    area = calcular_area(lado_a,lado_b,lado_c)
    print(f"El area de un triangulo de lados {lado_a}, {lado_b}, {lado_c} es {area}")

    return 0

if __name__ == "__main__":
    main()