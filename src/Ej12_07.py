#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def pedir_num():
    a = float(print("Dame un numero que sumar: "))
    return a


def suma(a,b,c):
    suma = a+b+c
    return suma


def main():
    a = pedir_num()
    b = pedir_num()
    c = pedir_num()
    suma = sum(a,b,c)

    print("La suma de ",a,", ",", ", " es ", suma)
    return 0

if __name__ == "__main__":
    main()