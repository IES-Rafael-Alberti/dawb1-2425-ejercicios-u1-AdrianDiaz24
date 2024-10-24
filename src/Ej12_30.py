# Escribir un programa que determine si un número es prim


def verificar_num(num):
    i = 1
    a = 0
    while i <= num:
        b = num%i
        if b == 0:
            a = a+1
            i = i+1
        else:
            i = i+1
    return a


def dar_resultado(a, num):
    if a <= 2:
        print(f"El {num} es un Nº primo.")
    else:
        print(f"El {num} no es un Nº primo.")
    return 0


def main():
    num = int(input("Dame un numero entero para comprobar si es primo: "))
    a = verificar_num(num)
    dar_resultado(a, num)
    return 0

if __name__ == "__main__":
    main()