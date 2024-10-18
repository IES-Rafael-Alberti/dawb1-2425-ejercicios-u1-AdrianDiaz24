# Escribir un programa que pida al usuario dos números enteros y muestre por 
# pantalla lo siguiente: "la división de n entre m da un cociente c 
# y un resto r", donde n y m son los números introducidos por el usuario, 
# y c y r son el cociente y el resto de la división entera respectivamente.


def pedir_dividendo():
    n = float(input("Dime un nº que dividir: "))
    return n


def pedir_divisor():
    m = float(input("Dime por que nº divides: "))
    return m


def calcular_resultado(n,m):
    c = n/m
    return c


def calcular_resto(n,m):
    r = n%m
    return r


def main():
    n = pedir_dividendo()
    m = pedir_divisor()
    c = calcular_resultado(n,m)
    r = calcular_resto(n,m)

    print(f"la división de {n} entre {m} da un cociente {c} y un resto ´{r}")
    return 0

if __name__ == "__main__":
    main()