# Escribir un programa que pregunte el nombre el un producto, su precio y un 
# número de unidades y muestre por pantalla una cadena con el nombre del producto 
# seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número 
# de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales


def precio_unitario(precio:str):
    a = precio.find(".")
    centimos = ".00"
    precio_u = "000000.00"
    i = -1
    if a == -1:
        precio = precio+centimos
    b = -1
    precio_u = precio.rjust(9,"0")

    return precio_u


def main ():
    nombre = str(input("Introduce el nombre del producto: "))
    precio = str(input("Introduce el precio unitario: "))
    unidades = str(input("Introduce el nº de unidades disponibles: "))
    precio_u = precio_unitario(precio)
    print(f"- {nombre} - {precio_u} - {unidades}")
    return 0

if __name__ == "__main__":
    main()