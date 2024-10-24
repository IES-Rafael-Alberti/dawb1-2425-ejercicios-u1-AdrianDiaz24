# Cálculo de un número aleatorio entre dos valores

import random

def dar_aleatorio(min, max):
    if min < max:
        num_aleatorio = random.randint(min,max)
        print(f"{num_aleatorio} es el numero aleatorio que te ha tocado entre {min} y {max}")
    else:
        num_aleatorio = random.randint(max, min)
        print(f"{num_aleatorio} es el numero aleatorio que te ha tocado entre {max} y {min}")
    return num_aleatorio

def main():

    min = int(input("Dame un numero entero:"))
    max  = int(input("Dame otro numero entero: "))

    dar_aleatorio(min, max)

    return 0

if __name__ == "__main__":
    main()