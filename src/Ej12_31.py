# Mostrar todos los divisores de un número


def decir_divisores(num):
    i = 1
    print(f"Los divisores de {num} son: ")
    while i <= num:
        if  num%i == 0:
            print (i)
            i = i+1
        else: 
            i = i+1
    return 0

def main():

    num = int(input("Dame un numero entero para decirte sus divisores: "))

    decir_divisores(num)

    return 0

if __name__ == "__main__":
    main()