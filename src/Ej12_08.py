#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

def pedir_num():
    a = float(input("Dame un numero que sumar: "))
    return a


def suma(a,resultado):
    resultado = resultado+a
    return resultado


def main():
    resultado = suma(0,0)
    a = pedir_num()
    resultado = suma(a,resultado)
    a = pedir_num()
    resultado = suma(a,resultado)
    a = pedir_num()
    resultado = suma(a, resultado)

    print("La suma de los numeros dados es ", resultado)
    return 0

if __name__ == "__main__":
    main()