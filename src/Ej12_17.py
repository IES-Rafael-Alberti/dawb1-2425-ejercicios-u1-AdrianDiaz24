# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces como el número introducido.


def pedir_nombre():
    nombre = str(input("Dime tu nombre: "))
    return nombre


def pedir_num():
    num = int(input("Dime un nº entero: "))
    return num


def comprobar_nombre(nombre:str):
     while nombre.isdigit():
          nombre = input("**ERROR** Esto no es un nombre, por favor introduzca uno valido: ")
     else:
        nombre = nombre.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
        return nombre


def mostrar_nombre(num, nombre):
        for i in range(num):
            print(nombre)
            i = i+1
        return i


def main():
    nombre = pedir_nombre()
    nombre = comprobar_nombre(nombre)
    num = pedir_num()
    mostrar_nombre(num,nombre)

if __name__ == "__main__":
    main()
