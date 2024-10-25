# Desarrolla una función en prueba1.py que reciba dos números y retorne el mayor número de los dos o 0 
# si son iguales. Realiza las pruebas unitarias y ejecútalas con pytest desde la terminal


def comprobar_num(a, b):
    if a < b:
        return b
    elif a > b:
        return b
    elif a == b:
        return 0

def main():
    a = int(input("Dame un numero entero: "))
    b = int(input("Dame otro numero entero: "))

    c = comprobar_num (a, b)

    print(f"El Nº mayor es {c}")

    return 0

if __name__ == "__main__":
    main()