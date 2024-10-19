# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces como el número introducido.


def pedir_nombre():
    nombre = str(input("Dime tu nombre: "))
    return nombre


def pedir_num():
    num = int(input("Dime un nº entero: "))
    return num


def main():
    nombre = pedir_nombre()
    num = pedir_num()
    i = 0


    return 0

if __name__ == "__main__":
    main()