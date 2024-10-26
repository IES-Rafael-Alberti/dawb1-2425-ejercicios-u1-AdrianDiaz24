# Calcular la serie de Fibonacci hasta un número dado


def sacar_serie(num):
    a = 1
    b = 0
    c = 1
    i = 0
    if num == 1:
        print(a)
    else:
        while i < num:
            print(c)
            c = a+b
            b = a
            a = c
            i = i+1
    return 0


def main():

    num = int(input("Dame un numero de veces que calcular la serie de Fibonacci: "))

    sacar_serie(num)

    return 0

if __name__ == "__main__":
    main()