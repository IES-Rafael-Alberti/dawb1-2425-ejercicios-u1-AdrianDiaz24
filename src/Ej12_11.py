#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después 
# muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
# La suma de los n primos enteros positivos puede ser calculada de la siguiente forma:
#suma =((n*(n+1))/2)

def pedir_num():
    num = float(input("Dame un numero: "))
    return num


def dar_num(a):
    i = 0
    while i < a:
        i = i+1
        print(i)
    return i



def main():
    a = pedir_num()
    dar_num(a)

    return 0

if __name__ == "__main__":
    main()
