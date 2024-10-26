#¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

def pedir_num():
    a = float(input("Dame un numero que sumar: "))
    return a


def suma(a,resultado):
    resultado = resultado+a
    return resultado


def main():

    return print("La suma de los numeros dados es ", suma(pedir_num(),suma(pedir_num(),suma(pedir_num(), 0))))

if __name__ == "__main__":
    main()