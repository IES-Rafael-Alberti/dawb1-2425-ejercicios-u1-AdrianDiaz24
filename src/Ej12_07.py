#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def pedir_num():
    a = float(input("Dame un numero que sumar: "))
    return a


def suma(a,b,c):
    resultado = a+b+c
    return resultado


def main():
    a = pedir_num()
    b = pedir_num()
    c = pedir_num()
    resultado = suma(a,b,c)

    print("La suma de ",a,", ",b,", ", c, " es ", resultado)
    return 0

if __name__ == "__main__":
    main()