# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
# muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número 
# de letras que tienen el nombre.


def pedir_nombre():
    nombre = str(input("Dame tu nombre: "))
    return nombre



def nombre_mayus(nombre:str):
    nombre_m = nombre.upper()
    return nombre_m


def contar_letras(nombre:str) -> bool:
    num_letras = 0
    while nombre.isalpha():
        num_letras = num_letras+1
    else:
        return num_letras


def main():
    nombre = pedir_nombre()
    nombre_m = nombre_mayus(nombre)
    a = contar_letras(nombre)

    print(f"{nombre_m} tiene {a} letras.")

    return 0

if __name__ == "__main__":
    main()